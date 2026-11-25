from django.db import migrations


def backfill_email_addresses(apps, schema_editor):
    FinanceUser = apps.get_model("authentification", "FinanceUser")
    EmailAddress = apps.get_model("account", "EmailAddress")
    database = schema_editor.connection.alias

    for user in FinanceUser.objects.using(database).exclude(email="").iterator():
        has_primary = EmailAddress.objects.using(database).filter(
            user_id=user.pk,
            primary=True,
        ).exists()
        EmailAddress.objects.using(database).get_or_create(
            user_id=user.pk,
            email=user.email,
            defaults={"primary": not has_primary, "verified": False},
        )


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0009_emailaddress_unique_primary_email"),
        ("authentification", "0002_financeuser_profile_fields"),
    ]

    operations = [
        migrations.RunPython(backfill_email_addresses, migrations.RunPython.noop),
    ]