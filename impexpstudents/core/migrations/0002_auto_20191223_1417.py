# Generated by Django 2.2.8 on 2019-12-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='IkiXxMTXZZ', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='TUser-rUser-VUser-XUser-BUser-rUser-EUser-nUser-tUser-V', max_length=50, unique=True),
        ),
    ]