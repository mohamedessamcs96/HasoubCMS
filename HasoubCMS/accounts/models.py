from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
from datetime import datetime as dt


TIMES_SLOTS = (
    ('7:30 - 8:30', '7:30 - 8:30'),
    ('8:30 - 9:30', '8:30 - 9:30'),
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('11:00 - 11:50', '11:00 - 11:50'),
    ('11:50 - 12:40', '11:50 - 12:40'),
    ('12:40 - 1:30', '12:40 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
)

SEMESTER_WEEKS=(
    ('1','Week 1'),
    ('2','Week 2'),
    ('3','Week 3'),
    ('4','Week 4'),
    ('5','Week 5'),
    ('6','Week 6'),
    ('7','Week 7'),
    ('8','Week 8'),
    ('9','Week 9'),
    ('10','Week 10'),
    ('11','Week 11'),
    ('12','Week 12'),
)
SEMESTER=(
('1','First Semester'),
('2','Second Semester'),
('3','Third Semester')
)
DAYS_OF_WEEK=(
    ('1','Sunday'),
    ('2','Monday'),
    ('3','Tuesday'),
    ('4','Wensday'),
    ('5','Thursday'),
)

GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female')
    )

class AppUser(AbstractUser):

    email=models.EmailField(max_length=50,unique=True)
    #USERNAME_FIELD='email'
    #REQUIRED_FIELDS=['email']
    parent_phone=models.CharField(max_length=18,default='+20')
    birthdate=models.DateField(null=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES, default='male')
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

class Course(models.Model):
    id = models.CharField(primary_key='True', max_length=50)
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=50, default='X')



class Class(models.Model):
    courses = models.ManyToManyField(Course, default=1)
    id = models.CharField(primary_key='True', max_length=100)
    section = models.CharField(max_length=100)
    
    


class Student(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, null=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)
    USN = models.CharField(primary_key='True', max_length=100)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=50, choices=GENDER_CHOICES, default='Male')
    DOB = models.DateField(default='1998-01-01')



class Teacher(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, null=True)
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=50, choices=GENDER_CHOICES, default='Male')
    DOB = models.DateField(default='1980-01-01')

class Semester(models.Model):
    sem = models.CharField(choices=SEMESTER,max_length=2,default='1',unique=True)
    def __str__(self):
        return self.sem
class Week(models.Model):
    week = models.CharField(choices=SEMESTER_WEEKS,max_length=2,default='1',unique=True)
    def __str__(self):
        return self.week
class Day(models.Model):
    day = models.CharField(choices=DAYS_OF_WEEK,max_length=2,default='1',unique=True)
    def __str__(self):
        return self.day

class AttendanceClass(models.Model):
    sem = models.OneToOneField(Semester, on_delete=models.CASCADE)
    week = models.OneToOneField(Week, on_delete=models.CASCADE)
    day = models.OneToOneField(Day, on_delete=models.CASCADE)
    date = models.DateField(default=str(dt.now().year)+'-'+str(dt.now().month)+'-'+str(dt.now().day))
    
    def __str__(self):
        return 'Semester '+str(self.sem)+'Week '+str(self.week)+'Day '+str(self.day)

class Attendance(models.Model):  
    student = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    attendanceclass = models.ForeignKey(AttendanceClass, on_delete=models.CASCADE, default=1,unique=True)
    status = models.BooleanField(default='True')
    def __str__(self):
        self.attendstatus='Attend' if self.status==True else 'Absent'
        #attendstatus=self.status.map({True:'Attend',False:'Absent'})
        return 'Student name:'+str(self.student)+'status: '+str(self.attendstatus)+'attend at:'+str(self.attendanceclass)

"""
    def __str__(self):
        sname = AppUser.objects.get(name=self.student)
        return '%s' % (sname.name)
"""




class Assign(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class AssignTime(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    period = models.CharField(max_length=50, choices=TIMES_SLOTS, default='11:00 - 11:50')
    day = models.CharField(max_length=15, choices=DAYS_OF_WEEK)



