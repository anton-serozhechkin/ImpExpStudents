# Generated by Django 2.2 on 2020-05-20 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200519_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_number',
            field=models.CharField(default='Невідомо', max_length=50, verbose_name='Номер студентського квитка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='KrSdLqrQBv', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='User-nqoqSWfPvZ', max_length=50, unique=True),
        ),
    ]
