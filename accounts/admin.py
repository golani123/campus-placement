from django.contrib import admin
from accounts.models import *

class UserAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','gender','role']

admin.site.register(User, UserAdmin)
# Register your models here.
