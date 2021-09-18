# Generated by Django 3.2.7 on 2021-09-08 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='flag',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[(0, 'ADMIN'), (1, 'TEACHER'), (2, 'STUDENT')], default=2, max_length=15),
        ),
    ]