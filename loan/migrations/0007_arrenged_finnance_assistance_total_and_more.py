# Generated by Django 5.0.2 on 2024-06-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0006_arrenged_finnance_assistance_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrenged_finnance_assistance',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='loan_expense_details',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]