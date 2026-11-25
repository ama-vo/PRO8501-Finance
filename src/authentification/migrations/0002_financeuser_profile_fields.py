from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentification", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="financeuser",
            name="country",
            field=models.CharField(default="France", max_length=100),
        ),
        migrations.AddField(
            model_name="financeuser",
            name="address",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="financeuser",
            name="phone",
            field=models.CharField(default="", max_length=20),
            preserve_default=False,
        ),
    ]