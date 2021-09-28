from os import read
from re import sub
from django.db.models import fields
from django.db.models.base import Model
from numpy.lib.utils import source
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from django.contrib.auth import get_user_model
from .models import SubjectDetail, FacultyDetail, Subject
from students.models import StudentDetail

User = get_user_model()

# Use it for multiple reading object(List)
class SubjectsListSerializer(serializers.ModelSerializer):
    subject_name = serializers.SerializerMethodField(source='skill_set')
    class Meta:
        model = SubjectDetail
        fields = ['subject_id', 'subject_name'] 

    def get_subject_name(self, instance):
        subject = Subject.objects.get(subject_id = instance.subject_id.subject_id)
        return subject.subject_name


# Use it for multiple reading object(List)
class StudentsListSerializer(serializers.ModelSerializer):

    sid = serializers.SerializerMethodField(source='skill_set')
    class Meta:
        model = StudentDetail
        fields = ['sid', 'name']     
    
    def get_sid(self, instance):
        return instance.sid.uid

