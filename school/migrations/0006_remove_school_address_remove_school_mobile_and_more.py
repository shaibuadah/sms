# Generated by Django 4.0 on 2023-09-17 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_school_address_school_mobile_school_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='address',
        ),
        migrations.RemoveField(
            model_name='school',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='school',
            name='state',
        ),
        migrations.RemoveField(
            model_name='school',
            name='user_profile',
        ),
    ]