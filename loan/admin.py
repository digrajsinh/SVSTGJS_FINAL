from django.contrib import admin

from loan.models import arrenged_finnance_assistance, loan_expense_details, request_edu_loan

# Register your models here.
admin.site.register(request_edu_loan)
admin.site.register(loan_expense_details)
admin.site.register(arrenged_finnance_assistance)