# Generated by Django 4.0 on 2023-09-17 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_rename_vendor_student_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='state',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]