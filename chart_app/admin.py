from django.contrib import admin
from .models import Uploadfiles

# Register your models here.

class UploadfilesAdmin(admin.ModelAdmin):
    list_display = ['file']

admin.site.register(Uploadfiles, UploadfilesAdmin)
