from django.contrib import admin
# Register your models here.
from .models import Record
# registering in the admin section
admin.site.register(Record)