
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from authentification.models import FinanceUser
from allauth.account.models import EmailAddress
import pyotp

PENDING_TOTP_USER_SESSION_KEY = "pending_totp_user_id"
PENDING_TOTP_ENROLLMENT_SECRET_SESSION_KEY = "pending_totp_enrollment_secret"


def visible_messages(request):
    return [
        message
        for message in messages.get_messages(request)
        if not str(message).startswith("A sign-in code has been sent to ")
    ]


def index(request):
    return render(request, "index.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            if user.totp_secret:
                request.session[PENDING_TOTP_USER_SESSION_KEY] = user.pk
                return redirect("totp_verify")

            login(request, user)
            return redirect("index")

        else:
            messages.error(request, "Wrong password or username.")
            return redirect("login")

    return render(request, "login/login.html", {"messages": visible_messages(request)})


def totp_verify(request):
    user_id = request.session.get(PENDING_TOTP_USER_SESSION_KEY)
    if user_id is None:
        return redirect("login")

    try:
        user = FinanceUser.objects.get(pk=user_id, is_active=True)
    except FinanceUser.DoesNotExist:
        request.session.pop(PENDING_TOTP_USER_SESSION_KEY, None)
        request.session.pop(PENDING_TOTP_ENROLLMENT_SECRET_SESSION_KEY, None)
        return redirect("login")

    enrollment_secret = request.session.get(
        PENDING_TOTP_ENROLLMENT_SECRET_SESSION_KEY
    )
    secret = enrollment_secret or user.totp_secret
    if not secret:
        request.session.pop(PENDING_TOTP_USER_SESSION_KEY, None)
        return redirect("login")

    error = None
    if request.method == "POST":
        if enrollment_secret and "skip_enrollment" in request.POST:
            request.session.pop(PENDING_TOTP_USER_SESSION_KEY, None)
            request.session.pop(PENDING_TOTP_ENROLLMENT_SECRET_SESSION_KEY, None)
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("index")

        code = request.POST.get("code", "").strip()
        if pyotp.TOTP(secret).verify(code, valid_window=1):
            if enrollment_secret:
                user.totp_secret = enrollment_secret
                user.save(update_fields=["totp_secret"])
            request.session.pop(PENDING_TOTP_USER_SESSION_KEY, None)
            request.session.pop(PENDING_TOTP_ENROLLMENT_SECRET_SESSION_KEY, None)
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("index")
        error = "Invalid verification code."

    return render(
        request,
        "totp.html",
        {
            "error": error,
            "enrollment_required": bool(enrollment_secret),
            "totp_secret": enrollment_secret,
        },
    )


def cancel_totp(request):
    request.session.pop(PENDING_TOTP_USER_SESSION_KEY, None)
    request.session.pop(PENDING_TOTP_ENROLLMENT_SECRET_SESSION_KEY, None)
    return redirect("login")


@require_POST
def logout_user(request):
    """Déconnecte l'utilisateur puis le redirige vers la page d'accueil."""
    logout(request)
    return redirect("index")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmedpassword = request.POST.get("confirmedpassword")

        if FinanceUser.objects.filter(username=username).exists():
            messages.error(request, "User already exists.")
            return redirect("signup")

        if not email:
            messages.error(request, "An email address is required.")
            return redirect("signup")

        if password != confirmedpassword:
            messages.error(request, "The password confirmation does not match.")
            return redirect("signup")

        new_user = FinanceUser.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname,
            email=email,
            password=password,
            address="",
            phone="",
        )
        EmailAddress.objects.create(
            user=new_user,
            email=email,
            primary=True,
        )
        request.session[PENDING_TOTP_USER_SESSION_KEY] = new_user.pk
        request.session[PENDING_TOTP_ENROLLMENT_SECRET_SESSION_KEY] = pyotp.random_base32()
        return redirect("totp_verify")

    return render(request, "signin/signup.html", {"messages": visible_messages(request)})
