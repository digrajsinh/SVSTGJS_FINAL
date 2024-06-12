from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Student_master, educational_details
from loan.models import arrenged_finnance_assistance, loan_expense_details, request_edu_loan





@login_required
def admin_loan_req_list(request):
    loan_list = request_edu_loan.objects.filter(status = 'REQUESTED')
    return render(request,'loan/admin/admin_loan_req_list.html',{'loan_list':loan_list})

@login_required
def admin_loan_aproved_list(request):
    loan_list = request_edu_loan.objects.filter(status = 'APPROVED')
    return render(request,'loan/admin/admin_loan_req_list.html',{'loan_list':loan_list})

@login_required
def admin_loan_rej_ret_list(request):
    loan_list = request_edu_loan.objects.filter(status__in = ('RETURN','REJECTED'))
    return render(request,'loan/admin/admin_loan_rej_ret_list.html',{'loan_list':loan_list})


@login_required
def admin_view_loan_details(request, id):
    request_data = get_object_or_404(Student_master, id=id)
    edu = educational_details.objects.filter(fkey=request_data)

    loan_proposed = request_edu_loan.objects.filter(student=request_data, status__in = ('REQUESTED','APPROVED'))

    loanObj = get_object_or_404(request_edu_loan, student=request_data, status__in = ('REQUESTED','APPROVED'))

    loan_expense = loan_expense_details.objects.filter(loan__in=loan_proposed)
    arranged_finnace = arrenged_finnance_assistance.objects.filter(fkzey__in=loan_proposed)

    return render(request, 'loan/admin/admin_view_loan_details.html', {'loanObj':loanObj,'reqObj': request_data, 'edu': edu,'loan_proposed':loan_proposed,'loan_expense':loan_expense,'arranged_finnace':arranged_finnace})













