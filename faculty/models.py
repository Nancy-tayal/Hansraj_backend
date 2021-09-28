from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from students.models import StudentDetail

# Create your models here.

User=get_user_model()

class ObjectDoesNotExistManager(models.Manager):
    def get_or_none(self, *args, **kwargs):
        qs = self.get_queryset().filter(*args, **kwargs)
        if qs.count() == 1:
            return qs.first()
        return None

class FacultyDetail(models.Model):
    tid= models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False)
    DEPARTMENT =(
        ('Anthropopgy', 'Anthropology'),
        ('Botany', 'Botany'),
        ('Chemistry', 'Chemistry'),
        ('Commerce', 'Commerce'),
        ('Computer Science', 'Computer Science'),
        ('Economics', 'Economics'),
        ('Electronics', 'Electronics'),
        ('English', 'English'),
        ('Geology', 'Geology'),
        ('Hindi', 'Hindi'),
        ('History', 'History'),
        ('Life Science', 'Life Science'),
        ('Mathematics', 'Mathematics'),
        ('Philosophy', 'Philosophy'),
        ('Physical Education', 'Physical Education'),
        ('Physics', 'Physics'),
        ('Sanskrit', 'Sanskrit'),
        ('Zoology', 'Zoology'),
    )
    department=models.CharField(choices=DEPARTMENT,max_length=50,null=False)
    email=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.tid.uid

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50,null=False)

    objects = ObjectDoesNotExistManager()

    def __str__(self):
        return self.subject_name + ' (' + str(self.subject_id) + ')'

class SubjectDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    tid=models.ForeignKey(FacultyDetail, on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)

    objects = ObjectDoesNotExistManager()

    def __str__(self):
        return str(self.subject_id.subject_name)+" by "+self.tid.name
    
'''@receiver(post_save, sender=User)
def create_faculty(sender, instance, **kwargs):
    if instance.role==User.STUDENT:
        StudentDetail.objects.create(sid=instance, email=instance.email)
    elif instance.role==User.TEACHER:
        FacultyDetail.objects.create(tid=instance, email=instance.email)'''