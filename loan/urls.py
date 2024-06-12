from django.urls import path
from loan.views import *
from loan.admin_loan_views import *


app_name = 'loan'

urlpatterns = [

    path('add_proposed_higher_page_details/<int:id>/',add_proposed_higher_page,name="add_proposed_higher_page_details"),
    path('edit_loan_details/<int:id>/', edit_loan_details, name='edit_loan_details'),
    path('delete_loan_proposed/<int:id>/', delete_proposed_higher, name='delete_loan_proposed'),



    path('education_expense_details/<int:id>/',education_expense_details,name="education_expense_details"),
    path('education-expense/<int:id>/<int:exp_id>/', education_expense_details, name='education_expense_details'),
    path('education-expense/delete/<int:exp_id>/', delete_education_expense, name='delete_education'),
    
    path('arranged_finance_details/<int:id>/', arranged_finance_details, name="arranged_finance_details"),
    path('edit_arranged_finance_detail/<int:id>/<int:detail_id>/', arranged_finance_details, name='edit_arranged_finance_detail'),
    path('delete_arranged_finance_detail/<int:id>/<int:detail_id>/', delete_arranged_finance_detail, name='delete_arranged_finance_detail'),



    #student loan list
    path('draft_loan_request_list/<int:id>/',draft_loan_request_list,name="draft_loan_request_list"),
    path('submit_loan_request/<int:id>/', submit_loan_request, name='submit_loan_request'),
    path('requested_loan_list/<int:id>/',requested_loan_list,name="requested_loan_list"),
    path('cancl_rej_loan_list/<int:id>/',cancl_rej_loan_list,name="cancl_rej_loan_list"),
    path('cancel_loan/<int:id>/', cancel_loan_request, name='cancel_loan'),

    # Admin loan list
    path('admin_loan_req_list/',admin_loan_req_list,name="admin_loan_req_list"),
    path('admin_loan_aproved_list/',admin_loan_aproved_list,name="admin_loan_aproved_list"),
    path('admin_loan_rej_ret_list/',admin_loan_rej_ret_list,name="admin_loan_rej_ret_list"),

    ##email url
    path('update-env/', update_env_vars, name='update_env_vars'),

    path('admin_view_loan_details/<int:id>/',admin_view_loan_details,name="admin_view_loan_details"),

    path('approve_stu_eduloan/<int:id>/', approve_stu_eduloan, name='approve_stu_eduloan'),
    path('reject_stu_eduloan/<int:id>/', reject_stu_eduloan, name='reject_stu_eduloan'),
    path('return_stu_eduloan/<int:id>/', return_stu_eduloan, name='return_stu_eduloan'),



]