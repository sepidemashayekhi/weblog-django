# Generated by Django 4.1.6 on 2023-02-23 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_ceates_post_ceated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ceated',
            new_name='created',
        ),
    ]
