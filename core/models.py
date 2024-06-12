from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager
from django.utils.translation import gettext_lazy as _



from django.apps import apps
from django.contrib import auth
from django.contrib.auth.hashers import make_password

# Create your models here.



class mtcom(models.Model):
    ip = models.GenericIPAddressField(null=True,blank=True)
    ua = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    modified_by = models.CharField(max_length=255, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True,null=True, blank=True)

    class Meta:
        abstract = True


class seriesMaster(mtcom):
    series=models.CharField(max_length=255, unique=True, null=True,blank=True)
    latest_usable_no  = models.IntegerField(default = 1)




class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        print(email, password, username, extra_fields)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()







class Staff(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        # unique=True,
        # help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        # validators=[username_validator],
        # error_messages={
        #     'unique': _("A user with that username already exists."),
        # },
        # default='',
        blank=True,
        null=True,
    )
    email = models.EmailField(_("email address"), unique=True)
    mobile=models.CharField(max_length=20,blank=True,null=True)
    gnati_no=models.CharField(max_length=50,blank=True,null=True)
    objects = CustomUserManager()
    USER_TYPE_CHOICES = (
        ('STUDENT', 'STUDENT'),
        ('PARENT', 'PARENT'),
        ('ADMIN', 'ADMIN'),
        # ('STUDENT', 'STUDENT'),
    )
    user_type = models.CharField(max_length=100, null=True, blank=True, choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return (str(self.email))
    
    @property
    def document_name(self):
        return f'{self.first_name} {self.last_name} - {self.id}'
    



def student_photo_path_path(instance, filename):
    return f"student_docs/{instance.member_id}/photo/{filename}"

class Student_master(Staff):
    TITLE_CHOICES = (
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Miss', 'Miss'),
        ('Ms.', 'Ms.'),
    )
    # user = models.ForeignKey(Staff, on_delete=models.CASCADE,null=True,blank=True)

    # student information
    passport_photo = models.ImageField(upload_to=student_photo_path_path, null=True, blank=True)
    aadhar_number = models.CharField(max_length=12, unique=True)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    # student_first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    # surname = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField()
    present_address = models.TextField(max_length=255)
    member_id = models.CharField(max_length=50, null=True, blank=True, unique=True) #autogenerate 
    # parent information
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    parent_title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    parent_first_name = models.CharField(max_length=50, null=True, blank=True)
    parent_father_name = models.CharField(max_length=50, null=True, blank=True)
    parent_surname = models.CharField(max_length=50, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    annual_income = models.IntegerField()
    parent_address = models.TextField(max_length=255)
    parent_mobile=models.CharField(max_length=20,blank=True,null=True)
    native_place = models.CharField(max_length=100, null=True, blank=True)


    # optional for another form filled
    edu = models.BooleanField(default=False,blank=True,null=True)
    prop = models.BooleanField(default=False,blank=True,null=True)
    ref = models.BooleanField(default=False,blank=True,null=True)
    doc= models.BooleanField(default=False,blank=True,null=True)
    apploan = models.BooleanField(default=False,blank=True,null=True)

    class Meta:
        verbose_name = "Student Master"



    @property
    def document_name(self):
        return f'{self.first_name} {self.last_name} - {self.member_id}'

class educational_details(mtcom):
    # details of education assistance outstanding by any other family members
    fkey = models.ForeignKey(Student_master, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50,blank=True,null=True)
    
    # education and carrier achivements 
    term_course_passed = models.CharField(max_length=200)
    passing_month_year = models.CharField(max_length=7)
    marks_grade_secured = models.CharField(max_length=4)
    marks_grade_outof = models.CharField(max_length=4)
    marks_grade_per = models.CharField(max_length=4)
    institute_university_name = models.CharField(max_length=150)


class two_reference(mtcom):
    TITLE_CHOICES = (
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Miss', 'Miss'),
        ('Ms.', 'Ms.'),
    )
    
    fkey = models.ForeignKey(Student_master, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    present_address = models.TextField(max_length=255)
    mobile_contact = models.CharField(max_length=15, null=True, blank=True)
    residence_contact = models.CharField(max_length=15, null=True, blank=True)




def student_doc_path_path(self, filename):
    return f"student_docs/{self.fkey.member_id}/{filename}"



class Upload_Documents(models.Model):
    fkey = models.ForeignKey(Student_master, on_delete=models.CASCADE,null=True,blank=True)
    upload_name = models.CharField(max_length=50)
    upload_file = models.ImageField(upload_to=student_doc_path_path)
   
