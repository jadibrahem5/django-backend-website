# Generated by Django 4.1 on 2022-12-31 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0021_routin_date_finish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routin',
            name='date_finish',
        ),
    ]
