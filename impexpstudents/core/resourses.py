from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export import resources
from .models import *

class UserResource(resources.ModelResource):
    last_name = Field(attribute='last_name', column_name='Прізвіще')
    first_name = Field(attribute='first_name', column_name="імя")
    middle_name = Field(attribute='middle_name', column_name='По батькові')
    user_type = Field(attribute='user_type', column_name='Тип користувача' )
    id_number = Field(attribute='id_number', column_name='Номер студентського квитка')
    

    class Meta:
        model = User
        import_id_fields = ('id_number',)
        exclude = ('year', 'academic_group_code', )
        fields = ('last_name',
                  'first_name', 'middle_name',
                  'user_type', 'id_number', )

class AcademicGroupResourse(resources.ModelResource):
    academic_group_code = Field(attribute='academic_group_code', column_name='Академічна група')
    class Meta:
        model = AcademicGroup
        import_id_fields = ('academic_group_code',)
        fields = ('academic_group_code', )
        exclude = ('last_name',
                  'first_name', 'middle_name',
                  'year', 'id_number', )

class StudentResourse(resources.ModelResource):
    user = Field(attribute='user', column_name='Користувач', widget=ForeignKeyWidget(User, 'id_number'))
    year = Field(attribute='year', column_name='Рік навчання')
    academic_group = Field(attribute='academic_group', column_name='Академычна група', widget=ForeignKeyWidget(AcademicGroup, 'academic_group_code'))

    class Meta:
        model = Student
        import_id_fields = ('user', )
        exclude = ('last_name','first_name',
         'middle_name','id_number', )
