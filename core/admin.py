from django.contrib import admin
from .models import Dessert 

class CoreAdmin(admin.ModelAdmin):
   readonly_fields = ('created','updated')

admin.site.register(Dessert, CoreAdmin)
