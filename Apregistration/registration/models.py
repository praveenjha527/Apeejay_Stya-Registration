from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Faculty(models.Model):
    class Meta:
        verbose_name= _("Faculty")
        verbose_name_plural= _("Faculties")

    TYPE_OF_FACULTY=(
        ('HOD','Head of Department'),
        ('D','DEAN'),
        ('AP','Associate-Professor'),
        ('L','Lab-Assistant'),
    )

    faculty_user=models.ForeignKey(User, unique=True)
    id=models.CharField(max_length=100, primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    Designation=models.CharField(max_length=4, choices=TYPE_OF_FACULTY)
    Department=models.CharField(max_length=100)

    def __unicode__(self):
        return  self.name

class course_details(models.Model):
    class Meta:
        verbose_name= _("Course Details")
        verbose_name_plural = _("Course_Details")

    COURSE_CHOICES=(
        ('D','DEGREE'),
        ('O','OPEN'),
        ('C','CORE')
    )
    code=models.CharField(max_length=100)
    type=models.CharField(max_length=1, choices=COURSE_CHOICES)
    title=models.CharField(max_length=100)
    University_sem=models.CharField(max_length=100)
    credit=models.IntegerField(default=None)
    faculty=models.ForeignKey(Faculty)

    def __unicode__(self):
        return self.code



class Student(models.Model):
    GENDER_CHOICES= (
        ('M','MALE'),
        ('F','FEMALE'),
    )
    class Meta:
        db_table = 'Student'
        app_label = 'registration'

    user=models.ForeignKey(User, unique=True)
    Enrollment_no=models.CharField(max_length=16, primary_key=True)
    Name=models.CharField(max_length=100)
    DOB=models.DateField()
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    Mobile_no=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    Father_Name =models.CharField(max_length=100)
    Father_mobile=models.CharField(max_length=100)
    Mother_name=models.CharField(max_length=100)
    Mother_mobile=models.CharField(max_length=100)
    Degree=models.CharField(max_length=100)
    Session=models.CharField(max_length=100)
    course=models.ForeignKey(course_details, null=True,default=None)
    Address=models.CharField(max_length=100)
    Mentor=models.ForeignKey(Faculty)

    def __unicode__(self):
        return self.Enrollment_no