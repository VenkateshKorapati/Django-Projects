# Generated by Django 4.0.2 on 2022-02-09 19:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vidz', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vidz',
            new_name='Vidzs',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='vidz',
            new_name='vidzs',
        ),
    ]
