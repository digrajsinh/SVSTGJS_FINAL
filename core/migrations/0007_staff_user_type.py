# Generated by Django 4.2.6 on 2024-05-31 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_student_master_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='user_type',
            field=models.CharField(blank=True, choices=[('STUDENT', 'STUDENT'), ('PARENT', 'PARENT'), ('ADMIN', 'ADMIN')], max_length=100, null=True),
        ),
    ]
