from django.db import models
from enum import Enum, unique
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
import random
import string
from slugify import slugify

def create_pass():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))

def create_log():
    letters = string.ascii_letters
    return slugify('User - ' + ''.join(random.choice(letters) for i in range(10)))


class Faculty(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='Назва факультету', null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Факультет'

    
class AcademicGroup(models.Model):
    academic_group_code = models.CharField(primary_key=True, max_length=50, verbose_name='Шифр навчальної групи')
    academic_group_faculty = models.ForeignKey('Faculty', models.DO_NOTHING, verbose_name='Факультет', null=True)

    def __str__(self):
        return self.academic_group_code

    class Meta:
        db_table = "Академічні групи"


class User(AbstractUser):
    first_name = models.CharField(max_length=30, default='')
    middle_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='') 
    password = models.CharField(max_length=50, default=create_pass())
    username = models.CharField(max_length=50, default=create_log(), unique=True)
    PRIORITIES = (
        (0, 'Викладач'),
        (1, 'Студент'),
    )
    user_type = models.PositiveSmallIntegerField(choices=PRIORITIES, default=1)
    id_number = models.CharField('Номер студентського квитка', max_length=50, unique=True, default='Невідомо')
    USERNAME_FIELD = 'id_number'

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, verbose_name='Користувач')
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)], default=1, verbose_name='Рік навчання')
    academic_group = models.ForeignKey('AcademicGroup', on_delete=models.DO_NOTHING, verbose_name='Академічна група')


    class Meta:
        db_table = "Студенти" 
