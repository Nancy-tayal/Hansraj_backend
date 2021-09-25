from django.db import models
from students.models import StudentDetail
from faculty.models import SubjectDetail

# Create your models here.

class Attendance(models.Model):
    sid=models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    detail_id=models.ForeignKey(SubjectDetail, on_delete=models.CASCADE)
    m1=models.IntegerField(null=True)
    m2=models.IntegerField(null=True)
    m3=models.IntegerField(null=True)
    m4=models.IntegerField(null=True)
    m5=models.IntegerField(null=True)
    m6=models.IntegerField(null=True)
    m7=models.IntegerField(null=True)
    m8=models.IntegerField(null=True)
    m9=models.IntegerField(null=True)
    m10=models.IntegerField(null=True)
    m11=models.IntegerField(null=True)
    m12=models.IntegerField(null=True)
    total=models.IntegerField(null=True)

    class Meta:
        db_table = 'Attendance'


class Attendance_Out_Of(models.Model):
    detail_id=models.ForeignKey(SubjectDetail, on_delete=models.CASCADE)
    m1=models.IntegerField(null=True)
    m2=models.IntegerField(null=True)
    m3=models.IntegerField(null=True)
    m4=models.IntegerField(null=True)
    m5=models.IntegerField(null=True)
    m6=models.IntegerField(null=True)
    m7=models.IntegerField(null=True)
    m8=models.IntegerField(null=True)
    m9=models.IntegerField(null=True)
    m10=models.IntegerField(null=True)
    m11=models.IntegerField(null=True)
    m12=models.IntegerField(null=True)
    total=models.IntegerField(null=True)
    
    class Meta:
        db_table = 'Attendance_Out_Of'
				
				
				
				
				
				
				
				
				
				