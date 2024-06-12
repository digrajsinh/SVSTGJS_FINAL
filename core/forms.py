from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Staff, Student_master, Upload_Documents, educational_details, two_reference





class RegistrationForm1(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('STUDENT', 'Student'),
        ('PARENT', 'Parent'),
    )
    email = forms.EmailField(label='E-mail', required=True)
    dob = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True, label="User Type")

    class Meta:
        model = Student_master
        fields = '__all__'
        exclude = ['date_joined', 'password', 'last_login', 'groups', 'user_permissions', 'is_superuser', 'is_staff', 'username',
                    'passport_photo', 'parent', 'parent_father_name', 'gnati_no', 'is_active']
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'}),
            'parent_title': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(RegistrationForm1, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True
            field.widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})
            if field_name in ['aadhar_number', 'first_name', 'last_name', 'email', 'mobile', 'password1', 'password2']:
                field.widget.attrs.update({'placeholder': field.label})
        # self.fields['aadhar_number'].widget.attrs['class'] = 'form-control'
        # self.fields['aadhar_number'].widget.attrs['placeholder'] = 'Aadhar No.'
        # self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        # self.fields['last_name'].widget.attrs['class'] = 'form-control'
        # self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        # self.fields['father_name'].widget.attrs['class'] = 'form-control'
        # self.fields['dob'].widget.attrs['class'] = 'form-control'
        # self.fields['present_address'].widget.attrs['class'] = 'form-control'
        # self.fields['parent_first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['parent_father_name'].widget.attrs['class'] = 'form-control'
        # self.fields['parent_surname'].widget.attrs['class'] = 'form-control'
        # self.fields['occupation'].widget.attrs['class'] = 'form-control'
        # self.fields['annual_income'].widget.attrs['class'] = 'form-control'
        # self.fields['parent_address'].widget.attrs['class'] = 'form-control'
        # self.fields['parent_mobile'].widget.attrs['class'] = 'form-control'
        # self.fields['mobile'].widget.attrs['class'] = 'form-control'
        # self.fields['mobile'].widget.attrs['placeholder'] = 'Mobile'
        # self.fields['native_place'].widget.attrs['class'] = 'form-control'
        # self.fields['email'].widget.attrs['class'] = 'form-control'
        # self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'
        # self.fields['user_type'].widget.attrs['class'] = 'form-control'




class StudentForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Student_master
        fields = '__all__'
        exclude = ['password', 'date_joined']
        
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'}),
            'parent_title': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['aadhar_number'].widget.attrs['class'] = 'form-control'
        self.fields['aadhar_number'].widget.attrs['placeholder'] = 'Aadhar No.'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['father_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['dob'].widget.attrs['class'] = 'form-control'
        self.fields['present_address'].widget.attrs['class'] = 'form-control'
        self.fields['parent_first_name'].widget.attrs['class'] = 'form-control'
        self.fields['parent_father_name'].widget.attrs['class'] = 'form-control'
        self.fields['parent_surname'].widget.attrs['class'] = 'form-control'
        self.fields['occupation'].widget.attrs['class'] = 'form-control'
        self.fields['annual_income'].widget.attrs['class'] = 'form-control'
        self.fields['parent_address'].widget.attrs['class'] = 'form-control'
        self.fields['parent_mobile'].widget.attrs['class'] = 'form-control'
        self.fields['mobile'].widget.attrs['class'] = 'form-control'
        self.fields['native_place'].widget.attrs['class'] = 'form-control'
        # self.fields['father_name'].widget.attrs['class'] = 'form-control'
        # self.fields['father_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        # self.fields['mobile'].widget.attrs['class'] = 'form-control'
        # self.fields['mobile'].widget.attrs['placeholder'] = 'Mobile'
        # self.fields['gnati_no'].widget.attrs['class'] = 'form-control'
        # self.fields['gnati_no'].widget.attrs['placeholder'] = 'Gnati Card No.'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'



class EditStudentForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Student_master
        fields = '__all__'
        exclude = ['password', 'date_joined', 'is_superuser', 'is_active', 'is_staff',  'user_type', 'parent']
        
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'}),
            'parent_title': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditStudentForm, self).__init__(*args, **kwargs)
        self.fields['aadhar_number'].widget.attrs['class'] = 'form-control'
        self.fields['aadhar_number'].widget.attrs['placeholder'] = 'Aadhar No.'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['father_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['dob'].widget.attrs['class'] = 'form-control'
        self.fields['present_address'].widget.attrs['class'] = 'form-control'
        self.fields['parent_first_name'].widget.attrs['class'] = 'form-control'
        self.fields['parent_father_name'].widget.attrs['class'] = 'form-control'
        self.fields['parent_surname'].widget.attrs['class'] = 'form-control'
        self.fields['occupation'].widget.attrs['class'] = 'form-control'
        self.fields['annual_income'].widget.attrs['class'] = 'form-control'
        self.fields['parent_address'].widget.attrs['class'] = 'form-control'
        self.fields['parent_mobile'].widget.attrs['class'] = 'form-control'
        self.fields['mobile'].widget.attrs['class'] = 'form-control'
        self.fields['native_place'].widget.attrs['class'] = 'form-control'
        # self.fields['father_name'].widget.attrs['class'] = 'form-control'
        # self.fields['father_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        # self.fields['mobile'].widget.attrs['class'] = 'form-control'
        # self.fields['mobile'].widget.attrs['placeholder'] = 'Mobile'
        # self.fields['gnati_no'].widget.attrs['class'] = 'form-control'
        # self.fields['gnati_no'].widget.attrs['placeholder'] = 'Gnati Card No.'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'

 

class EditChildrenForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Student_master
        fields = '__all__'
        exclude = ['password', 'date_joined', 'is_superuser', 'is_active', 'is_staff','user_type', 'parent']
        
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'}),
            'parent_title': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditChildrenForm, self).__init__(*args, **kwargs)
        self.fields['aadhar_number'].widget.attrs['class'] = 'form-control'
        self.fields['aadhar_number'].widget.attrs['placeholder'] = 'Aadhar No.'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['father_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['dob'].widget.attrs['class'] = 'form-control'
        self.fields['present_address'].widget.attrs['class'] = 'form-control'
        self.fields['parent_first_name'].widget.attrs['class'] = 'form-control'
        self.fields['parent_father_name'].widget.attrs['class'] = 'form-control'
        self.fields['parent_surname'].widget.attrs['class'] = 'form-control'
        self.fields['occupation'].widget.attrs['class'] = 'form-control'
        self.fields['annual_income'].widget.attrs['class'] = 'form-control'
        self.fields['parent_address'].widget.attrs['class'] = 'form-control'
        self.fields['parent_mobile'].widget.attrs['class'] = 'form-control'
        self.fields['mobile'].widget.attrs['class'] = 'form-control'
        self.fields['native_place'].widget.attrs['class'] = 'form-control'
        # self.fields['father_name'].widget.attrs['class'] = 'form-control'
        # self.fields['father_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        # self.fields['mobile'].widget.attrs['class'] = 'form-control'
        # self.fields['mobile'].widget.attrs['placeholder'] = 'Mobile'
        # self.fields['gnati_no'].widget.attrs['class'] = 'form-control'
        # self.fields['gnati_no'].widget.attrs['placeholder'] = 'Gnati Card No.'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'

 


class EducationFrom(forms.ModelForm):
    class Meta:
        model = educational_details
        fields = '__all__'

class ReferenceFrom(forms.ModelForm):
    class Meta:
        model = two_reference
        fields = '__all__'

    
class UploadFrom(forms.ModelForm):
    class Meta:
        model = Upload_Documents
        fields = '__all__'