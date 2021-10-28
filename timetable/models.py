from django.db import models
from faculty.models import Subject

# Create your models here.


# Create your models here.

class ObjectDoesNotExistManager(models.Manager):
    def get_or_none(self, *args, **kwargs):
        qs = self.get_queryset().filter(*args, **kwargs)
        if qs.count() == 1:
            return qs.first()
        return None


class Timetable(models.Model):
    COURSES= (
        ("B.Sc. (H) Botany","B.Sc. (H) Botany"),
        ("B.Sc. (H) Chemistry","B.Sc. (H) Chemistry"),
        ("B.Sc. (H) Computer Science","B.Sc. (H) Computer Science"),
        ("B.Sc. (H) Electronics","B.Sc. (H) Electronics"),
        ("B.Sc. (H) Mathematics","B.Sc. (H) Mathematics"),
        ("B.Sc. (H) Physics","B.Sc. (H) Physics"),
        ("B.Sc. (H) Zoology","B.Sc. (H) Zoology"),
        ("B.Com. (H)","B.Com. (H)"),
        ("B.A. (H) Economics","B.A. (H) Economics"),
        ("B.A. (H) English","B.A. (H) English"),
        ("B.A. (H) Hindi","B.A. (H) Hindi"),
        ("B.A. (H) History","B.A. (H) History"),
        ("B.A. (H) Philosophy","B.A. (H) Philosophy"),
        ("B.A. (H) Physical Education","B.A. (H) Physical Education"),
        ("B.A. (H) Sanskrit","B.A. (H) Sanskrit")
    )
    course=models.CharField(choices=COURSES, max_length=100)
    SEM= (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
    )
    semester=models.IntegerField(choices=SEM)    
    DAY= (
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
    )
    day =models.CharField(choices=DAY, max_length= 10)
    t1=models.ForeignKey(Subject,null=True, on_delete=models.CASCADE, related_name='time1', blank=True)    #8.40
    t2=models.ForeignKey(Subject,null=True, on_delete=models.CASCADE, related_name='time2', blank=True)    #9.40
    t3=models.ForeignKey(Subject,null=True, on_delete=models.CASCADE, related_name='time3', blank=True)    #10.40
    t4=models.ForeignKey(Subject,null=True, on_delete=models.CASCADE, related_name='time4', blank=True)    #11.40
    t5=models.ForeignKey(Subject,null=True, on_delete=models.CASCADE, related_name='time5', blank=True)    #1.00
    t6=models.ForeignKey(Subject,null=True, on_delete=models.CASCADE, related_name='time6', blank=True)    #2.00
    t7=models.ForeignKey(Subject,null=True, on_delete=models.CASCADE, related_name='time7', blank=True)    #3.00
    t8=models.ForeignKey(Subject,null=True, on_delete=models.CASCADE, related_name='time8', blank=True)    #4.00
    objects = ObjectDoesNotExistManager()

    class Meta:
        db_table = 'Timetable'

