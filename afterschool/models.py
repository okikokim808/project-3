from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    KINDERGARTEN = 'K'
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    FOURTH = '4'
    FIFTH = '5'
    SIXTH = '6'
    SEVENTH = '7'
    EIGHTH = '8'
    GRADE_CHOICE = (
    ('K', 'Kindergarten'),
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Third'),
    ('4', 'Fourth'),
    ('5', 'Fifth'),
    ('6', 'Sixth'),
    ('7', 'Seventh'),
    ('8', 'Eighth'),
)
    name = models.CharField(max_length=100)
    year_in_school = models.CharField(
        max_length=1,
        choices=GRADE_CHOICE,
        default=KINDERGARTEN,
    )
    id_pic = models.ImageField(upload_to='profile_pics',blank=True)
    student_id = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Parent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_pic = models.ImageField(upload_to='profile_pics',blank=True)
    students = models.ManyToManyField(Student,blank=True)
    balance_due = models.IntegerField()

    def __str__(self):
        return self.user.username

class DailyInfo(models.Model):
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    date = models.DateField()
    checkin = models.TimeField()
    checkout = models.TimeField()

    def __int__(self):
        return self.date
