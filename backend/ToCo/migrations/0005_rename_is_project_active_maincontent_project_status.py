# Generated by Django 5.0.3 on 2024-04-23 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToCo', '0004_maincontent_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maincontent',
            old_name='is_project_active',
            new_name='project_status',
        ),
    ]