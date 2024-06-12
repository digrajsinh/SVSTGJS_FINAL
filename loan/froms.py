from django import forms
from loan.models import arrenged_finnance_assistance, loan_expense_details, request_edu_loan



class EnvVarForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class RequestEduLoanForm(forms.ModelForm):
    class Meta:
        model = request_edu_loan
        fields = '__all__' 
        exclude = ['student','app_loan_amt','history_field']
        widgets = {
            'course_start': forms.DateInput(attrs={'type': 'date'}),
            'course_end': forms.DateInput(attrs={'type': 'date'}),
        }



class LoanExpenseDetailsForm(forms.ModelForm):
    class Meta:
        model = loan_expense_details
        fields = ['exp_date', 'exp_against_head', 'amt_payable', 'amt_arrenged', 'amt_shortfall']
        widgets = {
            'exp_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ArrangedFinanceForm(forms.ModelForm):
    class Meta:
        model = arrenged_finnance_assistance
        fields = '__all__'  # Include all fields

# class ProposedFrom(forms.ModelForm):
#     class Meta:
#         model = proposed_committed
#         fields = '__all__'


# class ArrangedFinancedFrom(forms.ModelForm):
#     class Meta:
#         model = arrenged_finnance_assistance
#         fields = '__all__'