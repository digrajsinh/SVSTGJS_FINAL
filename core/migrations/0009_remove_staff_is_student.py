# Generated by Django 5.0.2 on 2024-06-10 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_seriesmaster_educational_details_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='is_student',
        ),
    ]
