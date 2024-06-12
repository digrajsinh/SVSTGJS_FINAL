from datetime import datetime
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.db import IntegrityError
from django.contrib import messages
from core.models import Staff, Student_master, Upload_Documents, educational_details, two_reference
from loan.models import arrenged_finnance_assistance, loan_expense_details, request_edu_loan
from .forms import  EditChildrenForm, EducationFrom,ReferenceFrom, RegistrationForm1, StudentForm, UploadFrom, EditStudentForm
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.conf import settings
import os
from django.template.loader import get_template
from django.http import HttpResponse, FileResponse
from django.utils.encoding import force_bytes  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str
# Create your views here.

def home_page(request):
    return render(request,'forms/index.html')


@login_required
def view_filled_details_page(request):
    data = Student_master.objects.filter(parent__staff_ptr=request.user)
    return render(request, 'components/children_list.html',{'data':data})

@login_required
def view_student_profile(request,id):
    stuObj = get_object_or_404(Student_master, id=id)  
    if request.method == 'POST':
        form = EditChildrenForm(request.POST, request.FILES, instance=stuObj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Child details updated successfully.')
            return redirect('view_student_profile', id=id)
        else:
            messages.error(request, form.errors)

    else:
        form = EditChildrenForm(instance=stuObj)
    return render(request, 'components/edit_children_profile.html',{'form':form, 'student': stuObj})


def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        print(email)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login SuccessFully')
            if user.is_staff:
                return redirect('/')
            else:
                return redirect('personal_details')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request,"components/login.html")
    else:
        return render(request, "components/login.html")

 
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')





def activate(request, uidb64, token):  
    # User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = Student_master.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')  









def register_page_new(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['email'] = data['email'].lower()
        # data['is_active'] = False
        data['gnati_no'] = ''
        user_count = Student_master.objects.count()
        user_count +=1
        now = datetime.now()
        data['member_id'] = f'U{str(now.year)[-2:]}{user_count:05d}'
        form = RegistrationForm1(data, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            is_superuser = request.POST.get('is_superuser', False) == 'on'
            if is_superuser:
                user.is_staff = True
                user.save()
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('email/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            # messages.success(request, "User has been created successfully")
            messages.success(request, f'Registered Successfully... Activation link has been sent to your registered EMail id..."{to_email}" please click on the link to Activate ')
            return redirect("login")
        else:
            messages.error(request, form.errors)
            return render(request, 'components/register.html', {'form': form})
    else:
        form = RegistrationForm1()
        return render(request, 'components/register.html', {'form': form})



@login_required
def personal_details_page(request):
    if request.method == 'POST':
        data = (request.POST).copy()
        print(data)
        first_name = data['first_name']
        last_name = data['last_name']
        data['username'] = f"{first_name}.{last_name}".lower()
        username = f"{first_name}.{last_name}".lower()
        user_count = Student_master.objects.count()
        user_count +=1
        now = datetime.now()
        data['is_active']=True
        data['user_type'] = 'STUDENT'
        data['member_id'] = f'U{str(now.year)[-2:]}{user_count:05d}'
        form = StudentForm(data, request.FILES)
        if form.is_valid():
            try:
                student_master = form.save(commit=False)
                student_master.set_password(f'{first_name}@123')
                student_master.parent = Student_master.objects.get(staff_ptr = request.user)
                student_master.save()
                messages.success(request, f'Personal details submitted successfully. Username: {username}, Password: ')
                
                return redirect('/')
            except IntegrityError as e:
                if 'aadhar_number' in str(e):
                    messages.error(request, 'This Aadhar number is already registered.')
                else:
                    messages.error(request, 'An error occurred. Please try again.')
        else:
            messages.error(request, form.errors)
    else:
        form = StudentForm()
    return render(request, 'forms/add_child.html', {'form': form})



@login_required
def edit_personal_details(request,id):
    personal_detail = get_object_or_404(Student_master, id=id)  
    print(request.POST)
    if request.method == 'POST':
        form = EditStudentForm(request.POST, request.FILES, instance=personal_detail)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal details updated successfully.')
            return redirect('edit_personal_details', id=id)
        else:
            messages.error(request, form.errors)
    else:
        form = EditStudentForm(instance=personal_detail)
    return render(request, 'forms/edit_personal_details.html', {'form': form, 'student': personal_detail})


@login_required
def education_details_page(request,id):
    if request.method == 'POST':
        form = EducationFrom(request.POST)
        if form.is_valid():
            form.save()
            student = Student_master.objects.get(id=request.POST['fkey'])
            student.edu = True
            student.save() 
            messages.success(request, "Education details has been added successfully")
            return redirect('education_details',id)
    else:
            if request.method == 'GET':
                student = Student_master.objects.get(id=id)
                form = EducationFrom()
                edu = educational_details.objects.filter(fkey=student)
    return render(request, 'forms/educational_details.html',{'form':form,'student':student,'edu':edu})


@login_required
def edit_education_details(request, id):
    education_detail = get_object_or_404(educational_details, id=id)
    student = education_detail.fkey
    if request.method == 'POST':
        form = EducationFrom(request.POST, instance=education_detail)
        if form.is_valid():
            form.save()
            messages.success(request, "Education details has been updated successfully")
            return redirect('education_details',id=request.POST['fkey'])
    else:
        form = EducationFrom(instance=education_detail)
        edu = educational_details.objects.filter(fkey=student)
    return render(request, 'forms/educational_details.html', {'education_detail':education_detail,'form': form,'student': student,'edu': edu,'edu_id': id})

@login_required
def delete_education(request, id):
    edu = get_object_or_404(educational_details, id=id)
    student_id = edu.fkey.id
    edu.delete()
    messages.success(request, "Education details has been deleted successfully")
    return redirect('education_details', id=student_id)


@login_required
def reference_details_page(request,id):
    if request.method == 'POST':
        form = ReferenceFrom(request.POST)
        if form.is_valid():
            form.save()
            student = Student_master.objects.get(id=request.POST['fkey'])
            student.ref = True
            student.save()
            messages.success(request, "Reference details has been added successfully")
            return redirect('reference_details',id)
        else:
            messages.error(request, form.errors)
    else:
        if request.method == 'GET':
            student = Student_master.objects.get(id=id)
            ref = two_reference.objects.filter(fkey=student)
            form = ReferenceFrom()
    return render(request, 'forms/reference_details.html',{'form':form,'student':student,'ref':ref})


@login_required
def edit_reference_details(request, id):
    reference_detail = get_object_or_404(two_reference, id=id)
    student = reference_detail.fkey
    form = ReferenceFrom(instance=reference_detail)
    ref = two_reference.objects.filter(fkey=student)
    if request.method == 'POST':
        form = ReferenceFrom(request.POST, instance=reference_detail)
        if form.is_valid():
            form.save()
            messages.success(request, "Reference details has been updated successfully")
            return redirect('reference_details', id=student.id)
        else:
            messages.error(request, form.errors)
    else:
        form = ReferenceFrom(instance=reference_detail)
        ref = two_reference.objects.filter(fkey=student)
    return render(request, 'forms/reference_details.html', {'reference_details':reference_detail,'form': form,'student': student,'ref': ref,'ref_id': id})


@login_required
def delete_reference(request, id):
    reference = get_object_or_404(two_reference, id=id)
    student_id = reference.fkey.id
    reference.delete()
    messages.success(request, "Reference details has been deleted successfully")
    return redirect('reference_details', id=student_id)


@login_required
def upload_document_page(request,id):
    if request.method == 'POST':
        form = UploadFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            student = Student_master.objects.get(id=request.POST['fkey'])
            student.doc = True
            student.save()
            messages.success(request, "Document details has been added successfully")
            return redirect('upload_document_details',id)
    else:
            if request.method == 'GET':
                student = Student_master.objects.get(id=id)
                uploads = Upload_Documents.objects.filter(fkey=student)
                form = UploadFrom()
    return render(request, 'forms/upload_document.html',{'form':form,'student':student,'uploads':uploads})


@login_required
def edit_upload_document(request, id):
    upload_doc = get_object_or_404(Upload_Documents, id=id)
    student = upload_doc.fkey
    if request.method == 'POST':
        form = UploadFrom(request.POST, request.FILES, instance=upload_doc)
        if form.is_valid():
            form.save()
            messages.success(request, "Document details has been updated successfully")
            return redirect('upload_document_details', id=student.id)
    else:
        form = UploadFrom(instance=upload_doc)
        uploads = Upload_Documents.objects.filter(fkey=student)
    return render(request, 'forms/upload_document.html', {'form': form,'student': student,'uploads': uploads,'upd_id': id})

@login_required
def delete_document(request, id):
    doc = get_object_or_404(Upload_Documents, id=id)
    student_id = doc.fkey.id
    doc.delete()
    messages.success(request, "Document details has been deleted successfully")
    return redirect('upload_document_details', id=student_id)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'reset_password/password_reset.html'

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """Override send_mail method to send password reset emails only to registered users."""
        if User.objects.filter(email=to_email).exists():
            super().send_mail(subject_template_name, email_template_name,
                              context, from_email, to_email, html_email_template_name)
        else:
            return redirect('/')
        


############################ views  ####################################################################################################################

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # print(uri)
    result = finders.find(uri)
    if result:
            if not isinstance(result, (list, tuple)):
                    result = [result]
            result = list(os.path.realpath(path) for path in result)
            path=result[0]
    else:
            sUrl = settings.STATIC_URL        # Typically /static/
            sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL         # Typically /media/
            mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                    path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                    path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                    return uri

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    # context = Context(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment filename="report.pdf"'
    html  = template.render(context_dict)
    # result = StringIO.StringIO()
    # result_file = open('invoice.pdf', "w+b")
    pisa_status = pisa.CreatePDF(html, dest = response, link_callback=link_callback)
    # result_file.close()
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response
    return FileResponse(response, content_type='application/pdf')

    # 
    # pisa_status = pisa.CreatePDF(html, dest = response, link_callback=link_callback)
    # if pisa_status.err:
    #    return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response

def loan_pdf(request,id):
    loanObj = get_object_or_404(request_edu_loan, id=id)

    request_data = get_object_or_404(Student_master, id=loanObj.student.id)
    
    edu = educational_details.objects.filter(fkey=request_data)
    
    loan_proposed = request_edu_loan.objects.filter(student=request_data,status='APPROVED')
    
    loan_expense = loan_expense_details.objects.filter(loan__in=loan_proposed)
    
    arranged_finnace = arrenged_finnance_assistance.objects.filter(fkzey__in=loan_proposed)
    
    context={
        'request_data':request_data,
        'edu':edu,
        'loan_proposed':loan_proposed,
        'loan_expense':loan_expense,
        'arranged_finnace':arranged_finnace,
    }
    return render_to_pdf('svtg_loan_pdf.html',context)