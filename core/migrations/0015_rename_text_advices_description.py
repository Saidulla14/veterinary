# Generated by Django 3.2.5 on 2021-07-31 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210731_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advices',
            old_name='text',
            new_name='description',
        ),
    ]
