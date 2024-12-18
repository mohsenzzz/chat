# Generated by Django 4.2 on 2024-12-15 08:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0007_remove_chat_user_chat_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chat",
            name="user",
        ),
        migrations.AddField(
            model_name="chat",
            name="user",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="chats", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]