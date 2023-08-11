from django.contrib import admin
from .models import child
# Register your models here.

class ModelAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","joined_date")
    admin.site.register(child, child)




