# Generated by Django 4.1.6 on 2023-02-23 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ceates',
            new_name='ceated',
        ),
    ]
