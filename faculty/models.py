from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from students.models import StudentDetail

# Create your models here.

User=get_user_model()

class FacultyDetail(models.Model):
    tid= models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False)
    department=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.tid.uid

class SubjectDetail(models.Model):
    tid=models.ForeignKey(FacultyDetail, on_delete=models.CASCADE)
    subject_id=models.IntegerField()
    subject_name=models.CharField(max_length=50,null=False)

    def __str__(self):
        return str(self.subject_name)+" by "+self.tid.name
    
@receiver(post_save, sender=User)
def create_faculty(sender, instance, **kwargs):
    if instance.role==User.STUDENT:
        StudentDetail.objects.create(sid=instance, email=instance.email)
    elif instance.role==User.TEACHER:
        FacultyDetail.objects.create(tid=instance, email=instance.email)

