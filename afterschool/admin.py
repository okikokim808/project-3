from django.contrib import admin
from .models import Parent, Student, DailyInfo

admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(DailyInfo)
# Register your models here.
