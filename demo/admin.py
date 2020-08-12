from django.contrib import admin
from demo.models import Data

class DataAdmin(admin.ModelAdmin):
	list_display=['name','email','contact','password']

admin.site.register(Data,DataAdmin)
