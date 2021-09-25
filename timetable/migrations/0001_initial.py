# Generated by Django 3.2.7 on 2021-09-25 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('B.Sc. (H) Botany', 'B.Sc. (H) Botany'), ('B.Sc. (H) Chemistry', 'B.Sc. (H) Chemistry'), ('B.Sc. (H) Computer Science', 'B.Sc. (H) Computer Science'), ('B.Sc. (H) Electronics', 'B.Sc. (H) Electronics'), ('B.Sc. (H) Mathematics', 'B.Sc. (H) Mathematics'), ('B.Sc. (H) Physics', 'B.Sc. (H) Physics'), ('B.Sc. (H) Zoology', 'B.Sc. (H) Zoology'), ('B.Com. (H)', 'B.Com. (H)'), ('B.A. (H) Economics', 'B.A. (H) Economics'), ('B.A. (H) English', 'B.A. (H) English'), ('B.A. (H) Hindi', 'B.A. (H) Hindi'), ('B.A. (H) History', 'B.A. (H) History'), ('B.A. (H) Philosophy', 'B.A. (H) Philosophy'), ('B.A. (H) Physical Education', 'B.A. (H) Physical Education'), ('B.A. (H) Sanskrit', 'B.A. (H) Sanskrit')], max_length=100)),
                ('semester', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=10)),
                ('t1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time1', to='faculty.subject')),
                ('t2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time2', to='faculty.subject')),
                ('t3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time3', to='faculty.subject')),
                ('t4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time4', to='faculty.subject')),
                ('t5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time5', to='faculty.subject')),
                ('t6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time6', to='faculty.subject')),
                ('t7', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time7', to='faculty.subject')),
                ('t8', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='time8', to='faculty.subject')),
            ],
            options={
                'db_table': 'Timetable',
            },
        ),
    ]
