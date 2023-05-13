from django.contrib import admin
from jobsapp.models import *

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'location',  'created_at','category','company_name' )
    search_fields = ('title', 'description', 'location', 'salary')
    

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'user', 'created_at')
   

admin.site.register(Job, JobAdmin)
admin.site.register(Applicant, ApplicantAdmin)

# Register your models here.
