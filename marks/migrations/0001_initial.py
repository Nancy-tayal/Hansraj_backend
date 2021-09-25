# Generated by Django 3.2.7 on 2021-09-25 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks_Out_Of',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1', models.IntegerField(null=True)),
                ('a2', models.IntegerField(null=True)),
                ('a3', models.IntegerField(null=True)),
                ('a4', models.IntegerField(null=True)),
                ('a5', models.IntegerField(null=True)),
                ('a6', models.IntegerField(null=True)),
                ('a7', models.IntegerField(null=True)),
                ('a8', models.IntegerField(null=True)),
                ('a9', models.IntegerField(null=True)),
                ('a10', models.IntegerField(null=True)),
                ('i1', models.IntegerField(null=True)),
                ('i2', models.IntegerField(null=True)),
                ('i3', models.IntegerField(null=True)),
                ('practical', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.subjectdetail')),
            ],
            options={
                'db_table': 'Marks_Out_Of',
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1', models.IntegerField(null=True)),
                ('a2', models.IntegerField(null=True)),
                ('a3', models.IntegerField(null=True)),
                ('a4', models.IntegerField(null=True)),
                ('a5', models.IntegerField(null=True)),
                ('a6', models.IntegerField(null=True)),
                ('a7', models.IntegerField(null=True)),
                ('a8', models.IntegerField(null=True)),
                ('a9', models.IntegerField(null=True)),
                ('a10', models.IntegerField(null=True)),
                ('i1', models.IntegerField(null=True)),
                ('i2', models.IntegerField(null=True)),
                ('i3', models.IntegerField(null=True)),
                ('practical', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.subjectdetail')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentdetail')),
            ],
            options={
                'db_table': 'Marks',
            },
        ),
    ]
