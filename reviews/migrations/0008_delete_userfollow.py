# Generated by Django 3.2.9 on 2021-12-21 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_rename_userfollows_userfollow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFollow',
        ),
    ]
