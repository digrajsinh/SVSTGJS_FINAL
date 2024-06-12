from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.models import Student_master
from loan.froms import ArrangedFinanceForm, LoanExpenseDetailsForm, RequestEduLoanForm
from loan.models import arrenged_finnance_assistance, loan_expense_details, request_edu_loan
from datetime import datetime
from django.contrib import messages
from django.conf import settings
from .froms import EnvVarForm
import os
import environ

# Create your views here.


def get_financial_year_fun(date=None):
    
    fy = ''
    if not date:
        date = datetime.now()
   
    month = date.month
    year = int(str(date.year)[-2:])
    if month>3:
        fy = f'{year}-{year+1}'
    
    else:
        fy = f'{year-1}-{year}'
    return fy




def update_env_vars(request):
    if request.method == 'POST':
        form = EnvVarForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Update the .env file
            env_file_path = os.path.join(settings.BASE_DIR, '.env')
            with open(env_file_path, 'w') as env_file:
                env_file.write(f"EMAIL_HOST_USER='{email}'\n")
                env_file.write(f"EMAIL_HOST_PASSWORD='{password}'\n")

            # Reload environment variables
            env = environ.Env()
            env.read_env(env_file_path)
            messages.success(request, 'Responder E-mail details has been updated successfully.')
            return redirect('/')  # Redirect to a success page
    else:
        form = EnvVarForm(initial={'email': settings.EMAIL_HOST_USER, 'password': settings.EMAIL_HOST_PASSWORD})

    return render(request, 'loan/admin/update_email.html', {'form': form})




@login_required
def add_proposed_higher_page(request, id):
    student = get_object_or_404(Student_master, id=id)
    if request.method == 'POST':
        form = RequestEduLoanForm(request.POST)
        if form.is_valid():
            edu_loan = form.save(commit=False)
            edu_loan.student = student
            edu_loan.fy = get_financial_year_fun()
            edu_loan.year = datetime.now().year
            edu_loan.status = 'DRAFT'
            edu_loan.save()
            messages.success(request, 'Proposed details has been added successfully.')
            return redirect('loan:edit_loan_details', id=edu_loan.id)
        else:
            print(form.errors)
    else:
        form = RequestEduLoanForm()
    return render(request, 'loan/request_a_loan.html', {'form': form, 'student': student})

@login_required
def edit_loan_details(request, id):
    loanObj = get_object_or_404(request_edu_loan, id=id)  
    print(request.POST)
    if request.method == 'POST':
        form = RequestEduLoanForm(request.POST,instance=loanObj)
        if form.is_valid():
            proposed_details = form.save(commit=False)
            proposed_details.student = loanObj.student
            proposed_details.status = 'DRAFT'
            proposed_details.save()
            messages.success(request, 'Proposed details has been updated successfully.')
            return redirect('loan:edit_loan_details', id=id)
        else:
            messages.error(request, form.errors)
    else:
        form = RequestEduLoanForm(instance=loanObj)
    return render(request, 'loan/edit_loan_details.html', {'form': form, 'loanObj': loanObj})

@login_required
def delete_proposed_higher(request, id):
    loanObj = get_object_or_404(request_edu_loan, id=id)    
    if request.method == 'POST':
        loanObj.delete()
        messages.success(request, 'Proposed details has been deleted successfully.')
        return redirect('view_filled_details')
    return render(request, 'loan/confirm_delete.html', {'loanObj': loanObj})


@login_required
def submit_loan_request(request, id):
    loanObj = get_object_or_404(request_edu_loan, id=id)
    loanObj.status = 'REQUESTED'
    loanObj.save()
    messages.success(request, 'Loan Requested successfully.')
    return redirect('view_filled_details')

@login_required
def cancel_loan_request(request, id):
    loanObj = get_object_or_404(request_edu_loan, id=id)
    loanObj.status = 'CANCELLED'
    loanObj.cancl_reason = request.POST['cancel_reason']
    loanObj.save()
    messages.success(request, 'Loan Cancelled successfully.')
    return redirect('loan:edit_loan_details', id=loanObj.id)
    
 


@login_required
def education_expense_details(request, id, exp_id=None):
    loan = get_object_or_404(request_edu_loan, id=id)
    if exp_id:
        expense_detail = get_object_or_404(loan_expense_details, id=exp_id)
    else:
        expense_detail = None

    if request.method == 'POST':
        if expense_detail:
            form = LoanExpenseDetailsForm(request.POST, instance=expense_detail)
        else:
            form = LoanExpenseDetailsForm(request.POST)
        if form.is_valid():
            expense_detail = form.save(commit=False)
            expense_detail.loan = loan
            expense_detail.save()
            messages.success(request, 'Education expense detail added successfully.' if not exp_id else 'Education expense detail updated successfully.')
            return redirect('loan:education_expense_details', id=loan.id)
        else:
            messages.error(request, form.errors)
    else:
        if expense_detail:
            form = LoanExpenseDetailsForm(instance=expense_detail)
        else:
            form = LoanExpenseDetailsForm()
    edu_expenses = loan_expense_details.objects.filter(loan=loan)
    return render(request, 'loan/proposed_expense.html', {'form': form,'edu_expenses': edu_expenses,'loan': loan,'expense_detail': expense_detail})


@login_required
def delete_education_expense(request, exp_id):
    expense_detail = get_object_or_404(loan_expense_details, id=exp_id)
    loan_id = expense_detail.loan.id
    expense_detail.delete()
    messages.success(request, 'Education expense detail deleted successfully.')
    return redirect('loan:education_expense_details', id=loan_id)

@login_required
def arranged_finance_details(request, id, detail_id=None):
    loan = get_object_or_404(request_edu_loan, id=id)
    finance_details = arrenged_finnance_assistance.objects.filter(fkzey=loan)
    
    if detail_id:
        finance_detail = get_object_or_404(arrenged_finnance_assistance, id=detail_id)
    else:
        finance_detail = None
    if request.method == 'POST':
        if finance_detail:
            form = ArrangedFinanceForm(request.POST, instance=finance_detail)
        else:
            form = ArrangedFinanceForm(request.POST)
        if form.is_valid():
            finance_detail = form.save(commit=False)
            finance_detail.fkzey = loan
            finance_detail.save()
            messages.success(request, 'Finance detail added successfully.' if not detail_id else 'Finance detail updated successfully.')
            return redirect('loan:arranged_finance_details', id=loan.id)
        else:
            messages.error(request, 'There was an error with your form.')
    else:
        if finance_detail:
            form = ArrangedFinanceForm(instance=finance_detail)
        else:
            form = ArrangedFinanceForm()
    return render(request, 'loan/arranged_finance.html', {'form': form,'loan': loan,'finance_detail':finance_detail,'finance_details': finance_details,'detail_id': detail_id,})


@login_required
def delete_arranged_finance_detail(request, id, detail_id):
    finance_detail = get_object_or_404(arrenged_finnance_assistance, id=detail_id, fkzey_id=id)
    finance_detail.delete()
    messages.success(request, 'Finance detail deleted successfully.')
    return redirect('loan:arranged_finance_details', id=id)

@login_required
def approve_stu_eduloan(request, id):
    loanObj = get_object_or_404(request_edu_loan, id=id)  
    loanObj.status = 'APPROVED'
    try:
        stuObj = Student_master.objects.get(staff_ptr=request.user)
    except Student_master.DoesNotExist:
        print(f"No Student_master found for user: {request.user}")
        stuObj = request.user
    loanObj.app_by = stuObj.document_name
    loanObj.app_date = datetime.now()
    loanObj.save()
    return redirect('loan:admin_loan_req_list')


@login_required
def reject_stu_eduloan(request, id):
    loanObj = get_object_or_404(request_edu_loan, id=id)  
    loanObj.status = 'REJECTED'
    stuObj = Student_master.objects.get(staff_ptr = request.user)
    loanObj.app_by = stuObj.document_name
    loanObj.rej_date = datetime.now()
    loanObj.rej_reason = request.POST['rej_reason']
    loanObj.save()
    return redirect('loan:admin_loan_req_list')


@login_required
def return_stu_eduloan(request, id):
    loanObj = get_object_or_404(request_edu_loan, id=id)  
    loanObj.status = 'RETURN'
    stuObj = Student_master.objects.get(staff_ptr = request.user)
    loanObj.app_by = stuObj.document_name
    loanObj.ret_dt = datetime.now()
    loanObj.return_reason = request.POST['return_reason']
    loanObj.save()
    return redirect('loan:admin_loan_req_list')


@login_required
def draft_loan_request_list(request,id):
    studentObj = get_object_or_404(Student_master, id=id)
    loan_list = request_edu_loan.objects.filter(student = studentObj, status__in = ('DRAFT','RETURN'))
    return render(request,'loan/draft_loan_request.html',{'data':studentObj, 'loan_list':loan_list})


@login_required
def requested_loan_list(request,id):
    studentObj = get_object_or_404(Student_master, id=id)
    loan_list = request_edu_loan.objects.filter(student = studentObj, status__in =('REQUESTED','APPROVED'))
    return render(request,'loan/requested_loan_list.html',{'data':studentObj, 'loan_list':loan_list})


@login_required
def cancl_rej_loan_list(request,id):
    studentObj = get_object_or_404(Student_master, id=id)
    loan_list = request_edu_loan.objects.filter(student = studentObj, status__in = ('CANCELLED', 'REJECTED'))
    return render(request,'loan/cancl_rej_loan_list.html',{'data':studentObj, 'loan_list':loan_list})