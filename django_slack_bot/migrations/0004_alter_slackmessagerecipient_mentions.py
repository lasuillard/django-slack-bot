# Generated by Django 4.2.9 on 2024-01-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_slack_bot", "0003_auto_20231230_1249"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slackmessagerecipient",
            name="mentions",
            field=models.ManyToManyField(
                blank=True,
                help_text="List of mentions.",
                to="django_slack_bot.slackmention",
                verbose_name="Mentions",
            ),
        ),
    ]
