from django.db import models
from student.models import Student
from teacher.models import Teacher

class Course(models.Model):
    title = models.CharField(max_length=500)
    credit_hours = models.IntegerField()
    assigned_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    student = models.ManyToManyField(Student, through='Enrollment')


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    edited_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

