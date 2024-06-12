from django.urls import path
from core.views import *
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView

urlpatterns = [
    
    #root
    path('',home_page,name="home"),
    path('view_filled_details/',view_filled_details_page,name="view_filled_details"),
    path('view_student_profile/<int:id>/',view_student_profile,name="view_student_profile"),
    
    #login and register
    path('login/',login_page,name="login"),
    path('logout/',logout_view,name="logout"),
    path('register-new/',register_page_new,name="register-new"),

    #form
    path('personal_details/',personal_details_page,name="personal_details"),
    path('edit_personal_details/<int:id>/',edit_personal_details,name="edit_personal_details"),
    
    path('education_details/<int:id>/',education_details_page,name="education_details"),
    path('edit-education-details/<int:id>/', edit_education_details, name='edit_education_details'),
    path('delete_education/<int:id>/', delete_education, name='delete_education'),

    path('reference_details/<int:id>/',reference_details_page,name="reference_details"),
    path('edit_reference_details/<int:id>/',edit_reference_details,name="edit_reference_details"),
    path('delete_reference/<int:id>/', delete_reference, name='delete_reference'),
   
    path('upload_document_details/<int:id>/',upload_document_page,name="upload_document_details"),
    path('edit_upload_document/<int:id>/',edit_upload_document,name="edit_upload_document"),
    path('delete_document/<int:id>/', delete_document, name='delete_document'),

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='reset_password/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/password_reset_complete.html'), name='password_reset_complete'),

    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate'),  
    #pdf
    path('loan_pdf/<int:id>', loan_pdf, name='loan_pdf'),
]
