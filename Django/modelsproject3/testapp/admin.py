from django.contrib import admin
from testapp.models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['Author','Book_no','Book_Title','Published_date']
admin.site.register(Book,BookAdmin)
