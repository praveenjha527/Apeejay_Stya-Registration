from django.contrib import admin
from models import *
# Register your models here.



class Courseinline(admin.StackedInline):
    model = course_details
    fields=('code','type','title','University_sem','credit','faculty',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Enrollment_no', 'DOB', 'Degree', 'Session')
    list_filter = ('Degree', 'Session')
    search_fields = ('Enrollment_no', 'Name')
    inlines = [
        Courseinline,
    ]



class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'Department')
    list_filter = ('Designation', 'Department')
    search_fields = ('name', 'id')
    inlines = [
        Courseinline,
    ]

class courseAdmin(admin.ModelAdmin):
    list_display= ('code', 'title', 'type')
    list_filter= ('type',)
    search_fields= ('title',)



admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(course_details, courseAdmin)
