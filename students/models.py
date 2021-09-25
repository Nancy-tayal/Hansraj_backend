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
    university_roll_no=models.BigIntegerField(null=True)    
    COURSES= (
        ('B.Com. (H)', 'B.Com. (H)'),
        ("B.Sc. (H) Botany","B.Sc. (H) Botany"),
        ("B.Sc. (H) Chemistry","B.Sc. (H) Chemistry"),
        ("B.Sc. (H) Computer Science","B.Sc. (H) Computer Science"),
        ("B.Sc. (H) Electronics","B.Sc. (H) Electronics"),
        ("B.Sc. (H) Mathematics","B.Sc. (H) Mathematics"),
        ("B.Sc. (H) Physics","B.Sc. (H) Physics"),
        ("B.Sc. (H) Zoology","B.Sc. (H) Zoology"),
        ("B.A. (H) Economics","B.A. (H) Economics"),
        ("B.A. (H) English","B.A. (H) English"),
        ("B.A. (H) Hindi","B.A. (H) Hindi"),
        ("B.A. (H) History","B.A. (H) History"),
        ("B.A. (H) Philosophy","B.A. (H) Philosophy"),
        ("B.A. (H) Physical Education","B.A. (H) Physical Education"),
        ("B.A. (H) Sanskrit","B.A. (H) Sanskrit")
    )
    course=models.CharField(choices=COURSES, max_length=200)
    SEM= (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
    )
    semester=models.IntegerField(choices=SEM,null=True)    
    subject=models.ManyToManyField('faculty.SubjectDetail', blank=True)

    def __str__(self):
        return self.sid.uid
