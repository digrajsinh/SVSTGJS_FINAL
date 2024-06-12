from django.contrib import admin
from core.models import Staff, Student_master, Upload_Documents, educational_details, two_reference

# Register your models here.
admin.site.register(Staff)
admin.site.register(Student_master)
admin.site.register(two_reference)
admin.site.register(Upload_Documents)
admin.site.register(educational_details)
