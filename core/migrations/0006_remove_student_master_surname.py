# Generated by Django 4.2.6 on 2024-05-31 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_mobile_two_reference_mobile_contact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_master',
            name='surname',
        ),
    ]
