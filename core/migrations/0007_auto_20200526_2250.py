# Generated by Django 2.2 on 2020-05-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200526_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='oFtEmdIJnT', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='User-NPStbgIVTH', max_length=50, unique=True),
        ),
    ]
