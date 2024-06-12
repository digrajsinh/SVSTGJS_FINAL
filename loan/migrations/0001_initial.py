# Generated by Django 5.0.2 on 2024-05-29 12:47

import django.db.models.deletion
import loan.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_rename_mobile_two_reference_mobile_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='request_edu_loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank=True, max_length=255, null=True)),
                ('member_id', models.CharField(blank=True, max_length=50, null=True)),
                ('request_no', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('course', models.CharField(max_length=100)),
                ('duration', models.DecimalField(decimal_places=1, max_digits=2)),
                ('course_start', models.DateField(max_length=7)),
                ('course_end', models.DateField(max_length=7)),
                ('institute_name', models.CharField(max_length=100)),
                ('institute_address', models.TextField()),
                ('affiliated_university', models.CharField(max_length=100)),
                ('total_course_expense', models.IntegerField(default=0)),
                ('total_amt_arranged', models.IntegerField(default=0)),
                ('total_loan_amount', models.IntegerField(default=0)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.student_master')),
            ],
        ),
        migrations.CreateModel(
            name='loanDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_name', models.CharField(max_length=50)),
                ('upload_file', models.ImageField(upload_to=loan.models.loanDocs_path)),
                ('loan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loan.request_edu_loan')),
            ],
        ),
        migrations.CreateModel(
            name='loan_expense_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_date', models.DateField()),
                ('exp_against_head', models.CharField(max_length=100)),
                ('amt_payable', models.IntegerField(default=0)),
                ('amt_arrenged', models.IntegerField(default=0)),
                ('amt_shortfall', models.IntegerField(default=0)),
                ('loan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loan.request_edu_loan')),
            ],
        ),
        migrations.CreateModel(
            name='arrenged_finnance_assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revenu_head_details', models.CharField(max_length=100)),
                ('revenue_organization', models.CharField(max_length=100)),
                ('amount_payable', models.IntegerField(default=0)),
                ('amount_arranged', models.IntegerField(default=0)),
                ('amount_shortfiall', models.IntegerField(default=0)),
                ('fkzey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='loan.request_edu_loan')),
            ],
        ),
    ]