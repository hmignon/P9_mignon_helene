# Generated by Django 3.2.9 on 2021-12-18 18:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0006_userfollows'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFollows',
            new_name='UserFollow',
        ),
    ]
