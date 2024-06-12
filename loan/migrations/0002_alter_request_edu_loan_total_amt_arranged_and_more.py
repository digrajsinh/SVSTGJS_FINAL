# Generated by Django 5.0.2 on 2024-05-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_edu_loan',
            name='total_amt_arranged',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='request_edu_loan',
            name='total_course_expense',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='request_edu_loan',
            name='total_loan_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
