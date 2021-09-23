from django.db import models
from django.contrib.auth import get_user_model
# from faculty.models import SubjectDetail
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

User=get_user_model()

class StudentDetail(models.Model):
    sid= models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    name=models.CharField(max_length=50,null=True)
    university_roll_no=models.IntegerField(null=True)
    course=models.CharField(max_length=50,null=True)
    SEM= (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
    )
    semester=models.IntegerField(choices=SEM,null=True)    
    subject=models.ManyToManyField('faculty.SubjectDetail')

    def __str__(self):
        return self.sid.uid
