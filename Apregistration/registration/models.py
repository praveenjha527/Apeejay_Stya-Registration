from django.db import models
from django.contrib.auth.models import User
import json
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

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
    history = HistoricalRecords()

    def __unicode__(self):
        return  self.name

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
    Address=models.CharField(max_length=100)
    Mentor=models.ForeignKey(Faculty)
    history = HistoricalRecords()

    def __unicode__(self):
        return self.Enrollment_no

    def course_check(self):
        pass

class course_details(models.Model):
    class Meta:
        verbose_name= _("Course Details")
        verbose_name_plural = _("Course_Details")

    COURSE_CHOICES=(
        ('D','DEGREE'),
        ('O','OPEN'),
        ('C','CORE')
    )
    code=models.CharField(max_length=100,primary_key=True)
    type=models.CharField(max_length=1, choices=COURSE_CHOICES)
    pre_requisite=models.ManyToManyField('self',blank=True,null=True)
    title=models.CharField(max_length=100)
    University_sem=models.CharField(max_length=100)
    credit=models.IntegerField(default=None)
    faculty=models.ManyToManyField(Faculty,blank=True,null=True)
    # Registration=models.ForeignKey(Semester_Wise_Registration,default='')
    # category=models.CharField(max_length=3,choices=)
    history = HistoricalRecords()

    def __unicode__(self):
        return self.code

    def set_pre_requisite(self,x):
        self.pre_requisite=json.dumps(x)

    def get_pre_requisite(self,x):
        return json.loads(self.pre_requisite)

    def calculate_semester(self):
        pass


class Semester_Wise_Registration(models.Model):
    STATUS_CHOICES=(
        ('N','NOT-ATTEMPTED'),
        ('P','PASS'),
        ('I','IMPROVEMENT'),
        ('R','RE-APPEAR')
    )


    University_Sem=models.CharField(max_length=100)
    course=models.ManyToManyField(course_details)
    student=models.ForeignKey(Student)
    created_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True,null=True)
    status=models.CharField(max_length=3,choices=STATUS_CHOICES)


    class Meta:
        verbose_name= _("Course_Registration")
        verbose_name_plural= _("Course_Registrations")
        unique_together= ('student','University_Sem')


    def __unicode__(self):
        return self.University_Sem

    def max_min_courses(self):
        course=self.Course
        if course:
            print len(course)



