from django.test import TestCase
import re

from django.core import mail
from django.test import override_settings
from django.urls import reverse

from allauth.account.models import EmailAddress
from authentification.models import FinanceUser


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
class LoginCodeTests(TestCase):
	def setUp(self):
		self.user = FinanceUser.objects.create_user(
			username="testuser",
			email="test@example.com",
			password="StrongTestPassword123!",
			address="",
			phone="",
		)
		EmailAddress.objects.create(
			user=self.user,
			email=self.user.email,
			primary=True,
		)

	def begin_login(self):
		response = self.client.post(
			reverse("login"),
			{"login": "testuser", "password": "StrongTestPassword123!"},
		)
		self.assertRedirects(response, reverse("account_confirm_login_code"))
		self.assertEqual(len(mail.outbox), 1)
		self.assertEqual(mail.outbox[0].to, [self.user.email])
		match = re.search(r"\b\d{6}\b", mail.outbox[0].body)
		self.assertIsNotNone(match)
		return match.group()

	def test_password_login_sends_code_without_authenticating(self):
		self.begin_login()

		self.assertNotIn("_auth_user_id", self.client.session)

	def test_valid_code_finishes_login(self):
		code = self.begin_login()

		response = self.client.post(
			reverse("account_confirm_login_code"),
			{"code": code},
		)

		self.assertRedirects(response, reverse("index"))
		self.assertEqual(self.client.session.get("_auth_user_id"), str(self.user.pk))

	def test_invalid_code_does_not_authenticate(self):
		code = self.begin_login()
		wrong_code = "000000" if code != "000000" else "111111"

		self.client.post(
			reverse("account_confirm_login_code"),
			{"code": wrong_code},
		)

		self.assertNotIn("_auth_user_id", self.client.session)

	def test_back_button_cancels_pending_code_login(self):
		self.begin_login()

		response = self.client.post(reverse("cancel_login_code"))

		self.assertRedirects(response, reverse("login"))
		self.assertNotIn("account_login", self.client.session)

	def test_signup_redirects_to_code_page(self):
		response = self.client.post(
			reverse("signup"),
			{
				"username": "newuser",
				"firstname": "New",
				"lastname": "User",
				"email": "new@example.com",
				"password": "StrongTestPassword123!",
				"confirmedpassword": "StrongTestPassword123!",
			},
		)

		self.assertRedirects(response, reverse("account_confirm_login_code"))
		self.assertEqual(response.url, "/otp/")
		self.assertTemplateUsed(self.client.get(response.url), "login/otp.html")
		self.assertEqual(mail.outbox[0].to, ["new@example.com"])
		self.assertNotIn("_auth_user_id", self.client.session)
