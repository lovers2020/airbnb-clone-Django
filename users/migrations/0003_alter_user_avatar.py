# Generated by Django 5.0 on 2024-01-04 01:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.URLField(blank=True),
        ),
    ]
