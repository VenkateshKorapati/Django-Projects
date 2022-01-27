from django.contrib import admin
from editorapp.models import *
# Register your models here.
class FilmEditingAdmin(admin.ModelAdmin):
    list_display=['ShortFilms','Documentaries','MusicAlbums','FeatureFilms','AdFilms']

class WeddingEditingAdmin(admin.ModelAdmin):
    list_display=['PreWedding','PostWedding','Bride_Bridegroom','Haldi','Mehandi','FinalWedding']

class BirthdayEditingAdmin(admin.ModelAdmin):
    list_display=['FirstBirthday','MonthlyBirthday']

class BusinessEditingAdmin(admin.ModelAdmin):
    list_display=['CompanyProfile','ProductReview']

class OtherEditingAdmin(admin.ModelAdmin):
    list_display=['MatureFuntions','PregnantSpecial','Retirement']



admin.site.register(FilmEditing,FilmEditingAdmin)
admin.site.register(WeddingEditing,WeddingEditingAdmin)
admin.site.register(BirthdayEditing,BirthdayEditingAdmin)
admin.site.register(BusinessEditing,BusinessEditingAdmin)
admin.site.register(OtherEditing,OtherEditingAdmin)
    