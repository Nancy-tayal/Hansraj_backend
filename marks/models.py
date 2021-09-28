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

class Marks(models.Model):
    sid=models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    detail_id=models.ForeignKey(SubjectDetail, on_delete=models.CASCADE)
    a1=models.IntegerField(null=True)
    a2=models.IntegerField(null=True)
    a3=models.IntegerField(null=True)
    a4=models.IntegerField(null=True)
    a5=models.IntegerField(null=True)
    a6=models.IntegerField(null=True)
    a7=models.IntegerField(null=True)
    a8=models.IntegerField(null=True)
    a9=models.IntegerField(null=True)
    a10=models.IntegerField(null=True)
    i1=models.IntegerField(null=True)
    i2=models.IntegerField(null=True)
    i3=models.IntegerField(null=True)
    practical=models.IntegerField(null=True)
    total=models.IntegerField(null=True)

    class Meta:
        db_table = 'Marks'

class Marks_Out_Of(models.Model):
    detail_id=models.ForeignKey(SubjectDetail, on_delete=models.CASCADE)
    a1=models.IntegerField(null=True)
    a2=models.IntegerField(null=True)
    a3=models.IntegerField(null=True)
    a4=models.IntegerField(null=True)
    a5=models.IntegerField(null=True)
    a6=models.IntegerField(null=True)
    a7=models.IntegerField(null=True)
    a8=models.IntegerField(null=True)
    a9=models.IntegerField(null=True)
    a10=models.IntegerField(null=True)
    i1=models.IntegerField(null=True)
    i2=models.IntegerField(null=True)
    i3=models.IntegerField(null=True)
    practical=models.IntegerField(null=True)
    total=models.IntegerField(null=True)

    objects = ObjectDoesNotExistManager()

    class Meta:
        db_table = 'Marks_Out_Of'
