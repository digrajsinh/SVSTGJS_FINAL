# Generated by Django 4.2.6 on 2024-05-29 04:55

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=150, null=True, verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('gnati_no', models.CharField(blank=True, max_length=50, null=True)),
                ('is_student', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', core.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student_master',
            fields=[
                ('staff_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('passport_photo', models.ImageField(upload_to=core.models.student_photo_path_path)),
                ('aadhar_number', models.CharField(max_length=12, unique=True)),
                ('title', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Miss', 'Miss'), ('Ms.', 'Ms.')], max_length=10)),
                ('father_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('present_address', models.TextField(max_length=255)),
                ('member_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('parent_title', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Miss', 'Miss'), ('Ms.', 'Ms.')], max_length=10)),
                ('parent_first_name', models.CharField(max_length=50)),
                ('parent_father_name', models.CharField(max_length=50)),
                ('parent_surname', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=100)),
                ('annual_income', models.IntegerField()),
                ('parent_address', models.TextField(max_length=255)),
                ('parent_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('native_place', models.CharField(max_length=100)),
                ('edu', models.BooleanField(blank=True, default=False, null=True)),
                ('prop', models.BooleanField(blank=True, default=False, null=True)),
                ('ref', models.BooleanField(blank=True, default=False, null=True)),
                ('doc', models.BooleanField(blank=True, default=False, null=True)),
                ('apploan', models.BooleanField(blank=True, default=False, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.student_master')),
            ],
            options={
                'verbose_name': 'Student Master',
            },
            bases=('core.staff',),
            managers=[
                ('objects', core.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Upload_Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_name', models.CharField(max_length=50)),
                ('upload_file', models.ImageField(upload_to=core.models.student_doc_path_path)),
                ('fkey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.student_master')),
            ],
        ),
        migrations.CreateModel(
            name='two_reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Miss', 'Miss'), ('Ms.', 'Ms.')], max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('present_address', models.TextField(max_length=255)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('fkey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.student_master')),
            ],
        ),
        migrations.CreateModel(
            name='educational_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank=True, max_length=50, null=True)),
                ('term_course_passed', models.CharField(max_length=200)),
                ('passing_month_year', models.CharField(max_length=7)),
                ('marks_grade_secured', models.CharField(max_length=4)),
                ('marks_grade_outof', models.CharField(max_length=4)),
                ('marks_grade_per', models.CharField(max_length=4)),
                ('institute_university_name', models.CharField(max_length=150)),
                ('fkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student_master')),
            ],
        ),
    ]
