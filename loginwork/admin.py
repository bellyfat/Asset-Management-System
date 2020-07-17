from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(userstable)
admin.site.register(assetstable)
admin.site.register(elementstable)
admin.site.register(purchasestable)
admin.site.register(sessiontable)