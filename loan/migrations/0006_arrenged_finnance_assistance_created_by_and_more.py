# Generated by Django 5.0.2 on 2024-06-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_rename_total_loan_amount_request_edu_loan_tot_req_loan_amt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrenged_finnance_assistance',
            name='created_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='arrenged_finnance_assistance',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='arrenged_finnance_assistance',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arrenged_finnance_assistance',
            name='modified_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='arrenged_finnance_assistance',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='arrenged_finnance_assistance',
            name='ua',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]