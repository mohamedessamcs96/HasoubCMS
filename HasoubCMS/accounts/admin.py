from django.contrib import admin
from .models import AppUser
from django.contrib.auth.models import Group

from accounts import models
# Register your models here.

class AppUserAdmin(admin.ModelAdmin):
    fields=('email','username','parent_phone','birthdate','gender','is_admin','is_superuser','is_staff')
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False



from .models import Attendance,AttendanceClass,Student,Teacher,Class,Week,Day,Semester,Course

admin.site.site_header="Hasoub CMS Admin Panel"
admin.site.site_title="Hasoub CMS Admin Panel"
#admin.site.index_template='templates/base.html'


admin.site.register(Attendance)
admin.site.register(AttendanceClass)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Semester)
admin.site.register(Week)
admin.site.register(Day)
admin.site.register(Course)
admin.site.register(AppUser,AppUserAdmin)
admin.site.unregister(Group)