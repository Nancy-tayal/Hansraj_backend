from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()

class StudentDetails(models.Model):
    uid= models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False)
    university_roll_no=models.IntegerField(null=False)
    course=models.CharField(max_length=50,null=True)
    
