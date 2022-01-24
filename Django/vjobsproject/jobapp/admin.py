from django.contrib import admin

from jobapp.models import Job
from jobapp.models import HydJobs
from jobapp.models import BlrJobs
from jobapp.models import ChennaiJobs
from jobapp.models import PuneJobs
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class HydJobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class BlrJobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class ChennaiJobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
class PuneJobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Job,JobAdmin)
admin.site.register(HydJobs,HydJobAdmin)
admin.site.register(BlrJobs,BlrJobAdmin)
admin.site.register(ChennaiJobs,ChennaiJobAdmin)
admin.site.register(PuneJobs,PuneJobAdmin)
