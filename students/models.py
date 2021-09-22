from django.db import models
from django.contrib.auth import get_user_model
from faculty.models import SubjectDetails

# Create your models here.

User=get_user_model()

class StudentDetails(models.Model):
    uid= models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    name=models.CharField(max_length=50,null=False)
    university_roll_no=models.IntegerField(null=False)
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
    subject=models.ManyToManyField(SubjectDetails)