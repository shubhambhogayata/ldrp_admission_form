from django.contrib import admin
from .models import formTable
from import_export.admin import ExportActionMixin
# Register your models here.

class FormTableAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("Student_Photo","ACPCRank","DOB","GUJCETRollNo","date","nameOfTheStudent","studentEmail","studentMobileNo1")
    search_fields = ("ACPCRank","DOB","GUJCETRollNo","date","nameOfTheStudent","studentEmail")

admin.site.register(formTable,FormTableAdmin)