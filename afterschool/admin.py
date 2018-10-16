from django.contrib import admin
from .models import Parent, Student, DailyInfo, MyModelAdmin

admin.site.register(Parent, MyModelAdmin)
admin.site.register(Student)
admin.site.register(DailyInfo)
# Register your models here.