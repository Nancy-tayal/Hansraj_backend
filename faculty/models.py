from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()

class FacultyDetails(models.Model):
    tid= models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False)
    department=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=100,null=False)

class SubjectDetails(models.Model):
    tid=models.ForeignKey(FacultyDetails, on_delete=models.CASCADE)
    subject_id=models.AutoField(primary_key = True)
    subject_name=models.CharField(max_length=50,null=False)
    