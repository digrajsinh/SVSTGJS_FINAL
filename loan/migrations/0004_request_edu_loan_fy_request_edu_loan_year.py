# Generated by Django 4.2.6 on 2024-05-31 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_request_edu_loan_date_request_edu_loan_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_edu_loan',
            name='fy',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='request_edu_loan',
            name='year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]