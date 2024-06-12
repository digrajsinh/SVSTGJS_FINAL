from django.db import models
from core.models import Student_master, mtcom
from datetime import datetime
from jsonfield import JSONField

# Create your models here.




# proposed committed - higher education study details
class request_edu_loan(mtcom):
    student = models.ForeignKey(Student_master, on_delete=models.CASCADE,null=True,blank=True)
    student_name = models.CharField(max_length=255,null=True, blank=True)
    member_id = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    
    request_no = models.CharField(max_length=50, null=True, blank=True, unique=True) #autogenerate
    course =  models.CharField(max_length=100)
    duration = models.DecimalField(decimal_places=1,max_digits=2)
    course_start = models.DateField(max_length=7)
    course_end = models.DateField(max_length=7)
    institute_name = models.CharField(max_length=100)
    institute_address = models.TextField()
    affiliated_university = models.CharField(max_length=100)

    total_course_expense = models.IntegerField(default=0,blank=True,null=True)
    total_amt_arranged = models.IntegerField(default=0,blank=True,null=True)
    tot_req_loan_amt = models.IntegerField(default=0,blank=True,null=True)
    
    status = models.CharField(max_length=255, null=True, blank=True)
    fy = models.CharField(max_length=10, null=True, blank=True)
    year = models.CharField(max_length=10, null=True, blank=True)



    app_by = models.CharField(max_length=255, null=True, blank=True)
    app_date = models.DateTimeField(null=True, blank=True)
    app_loan_amt = models.IntegerField(default=0)
    
    rej_by = models.CharField(max_length=255, null=True, blank=True)
    rej_date = models.DateTimeField(null=True, blank=True)
    rej_reason = models.TextField(null=True, blank=True)

    cancl_reason = models.TextField(null=True, blank=True)

    ret_by = models.CharField(max_length=255, null=True, blank=True)
    ret_dt = models.DateTimeField(null=True, blank=True)
    return_reason = models.TextField(null=True, blank=True)

    history_field = JSONField(default="{}")

# proposed committed education expense details
class loan_expense_details(mtcom):
    loan = models.ForeignKey(request_edu_loan, on_delete=models.CASCADE, null=True, blank=True)
    exp_date = models.DateField()
    exp_against_head = models.CharField(max_length=100)
    amt_payable = models.IntegerField(default=0)
    amt_arrenged = models.IntegerField(default=0)
    amt_shortfall = models.IntegerField(default=0)
    total = models.IntegerField(default=0,blank=True,null=True)


class arrenged_finnance_assistance(mtcom):
    fkzey = models.ForeignKey(request_edu_loan, on_delete=models.CASCADE,null=True,blank=True)
    revenu_head_details = models.CharField(max_length=100)
    revenue_organization = models.CharField(max_length=100)
    amount_payable = models.IntegerField(default=0)
    amount_arranged = models.IntegerField(default=0)
    amount_shortfiall = models.IntegerField(default=0)
    total = models.IntegerField(default=0,blank=True,null=True)



def loanDocs_path(instance, filename):
    now = datetime.now()
    return f"loan_docs/{now.year}/{instance.loan.request_no}/{filename}"


class loanDocuments(mtcom):
    loan = models.ForeignKey(request_edu_loan, on_delete=models.CASCADE,null=True,blank=True)
    upload_name = models.CharField(max_length=50)
    upload_file = models.ImageField(upload_to=loanDocs_path)
   
