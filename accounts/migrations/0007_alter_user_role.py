# Generated by Django 3.2.7 on 2021-09-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'ADMIN'), (1, 'TEACHER'), (2, 'STUDENT')], null=True),
        ),
    ]
