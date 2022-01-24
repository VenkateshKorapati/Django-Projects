from django.contrib import admin
from testapp.models import Job
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display=['Posting_date','Location','Offered_salary','Qualification']
admin.site.register(Job,JobAdmin)
