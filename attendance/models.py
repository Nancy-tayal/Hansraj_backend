from django.db import models
from students.models import StudentDetail
from faculty.models import SubjectDetail

# Create your models here.

class ObjectDoesNotExistManager(models.Manager):
    def get_or_none(self, *args, **kwargs):
        qs = self.get_queryset().filter(*args, **kwargs)
        if qs.count() == 1:
            return qs.first()
        return None


class Attendance(models.Model):
    sid=models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    detail_id=models.ForeignKey(SubjectDetail, on_delete=models.CASCADE)
    m1=models.IntegerField(null=True, default= 0)
    m2=models.IntegerField(null=True, default= 0)
    m3=models.IntegerField(null=True, default= 0)
    m4=models.IntegerField(null=True, default= 0)
    m5=models.IntegerField(null=True, default= 0)
    m6=models.IntegerField(null=True, default= 0)
    m7=models.IntegerField(null=True, default= 0)
    m8=models.IntegerField(null=True, default= 0)
    m9=models.IntegerField(null=True, default= 0)
    m10=models.IntegerField(null=True, default= 0)
    m11=models.IntegerField(null=True, default= 0)
    m12=models.IntegerField(null=True, default= 0)
    total=models.IntegerField(null=True, default= 0)

    class Meta:
        db_table = 'Attendance'


class Attendance_Out_Of(models.Model):
    detail_id=models.ForeignKey(SubjectDetail, on_delete=models.CASCADE)
    m1=models.IntegerField(null=True, default= 0)
    m2=models.IntegerField(null=True, default= 0)
    m3=models.IntegerField(null=True, default= 0)
    m4=models.IntegerField(null=True, default= 0)
    m5=models.IntegerField(null=True, default= 0)
    m6=models.IntegerField(null=True, default= 0)
    m7=models.IntegerField(null=True, default= 0)
    m8=models.IntegerField(null=True, default= 0)
    m9=models.IntegerField(null=True, default= 0)
    m10=models.IntegerField(null=True, default= 0)
    m11=models.IntegerField(null=True, default= 0)
    m12=models.IntegerField(null=True, default= 0)
    total=models.IntegerField(null=True, default= 0)


    objects = ObjectDoesNotExistManager()

    
    class Meta:
        db_table = 'Attendance_Out_Of'
				
				
				
				
				
				
				
				
				
				