from django.contrib import admin
from .models import Course, Enrollment,Semester

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Semester)