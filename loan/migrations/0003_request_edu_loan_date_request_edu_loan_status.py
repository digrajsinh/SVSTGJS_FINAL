# Generated by Django 4.2.6 on 2024-05-31 09:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_alter_request_edu_loan_total_amt_arranged_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_edu_loan',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request_edu_loan',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
