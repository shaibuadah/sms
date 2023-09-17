# Generated by Django 4.0 on 2023-09-17 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='user_profile',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='authentication.userprofile'),
            preserve_default=False,
        ),
    ]
