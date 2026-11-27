from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentification", "0002_financeuser_profile_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="financeuser",
            name="totp_secret",
            field=models.CharField(blank=True, default="", max_length=64),
        ),
    ]