# Generated by Django 4.2.4 on 2023-09-18 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_remove_school_address_remove_school_mobile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='is_due4payment',
            new_name='payment_status',
        ),
        migrations.AddField(
            model_name='student',
            name='bank_name',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='fname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='lname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='matric_no',
            field=models.CharField(default=1, max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_department', to='school.department'),
        ),
    ]