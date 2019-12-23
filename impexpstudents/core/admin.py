from django.contrib import admin
from .models import *
from django.contrib.auth.admin import Group
from .resourses import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


class UserAdmin(ImportExportModelAdmin):
    list_display = ('last_name',
                    'first_name', 'middle_name',
                    'user_type', 'id_number', )
    search_fields = ('first_name',
                     'middle_name',
                     'last_name', )
    resource_class = UserResource


class StudentAdmin(ImportExportModelAdmin):
    list_display = ('user', 'year', 'academic_group', )
    resource_class = StudentResourse


class AcademicGroupAdmin(ImportExportModelAdmin):
    list_display = ('academic_group_code', 'academic_group_faculty', )
    list_filter = ('academic_group_faculty', )
    resource_class = AcademicGroupResourse

 
class FacultyAdmin(admin.ModelAdmin):
    list_filter = ('name', )


admin.site.register(User, UserAdmin)
admin.site.register(Faculty)
admin.site.register(AcademicGroup, AcademicGroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.unregister(Group)