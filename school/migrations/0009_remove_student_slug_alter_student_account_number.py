# Generated by Django 4.2.4 on 2023-09-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_remove_student_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='slug',
        ),
        migrations.AlterField(
            model_name='student',
            name='account_number',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
