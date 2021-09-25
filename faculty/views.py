from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes,api_view
from django.core.mail import EmailMessage
from django.conf import settings
import secrets
import string
import pandas as pd
from .models import SubjectDetail, Subject, FacultyDetail
# Create your views here.
User = get_user_model()


def addSubjects(subj):
    subject =  Subject.objects.create(subject_name = subj['subject_name'])
    subject.save()


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def subjects(request):
    if request.data.get('file') is None :
        return Response({'message':'Please Provide the excel file'},status=status.HTTP_400_BAD_REQUEST)
    
    df = pd.read_excel(request.data.get('file'))
    df.apply(addSubjects, axis=1)
    return Response({'message':'Subjects added successfully'},status=status.HTTP_200_OK)
    


def addTeachers(teacher):
    faculty =  FacultyDetail.objects.create(tid = User.objects.get(uid = teacher['tid']), name = teacher['name'], email = teacher['email'], department = teacher['department'])
    faculty.save()


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def teachers(request):
    if request.data.get('file') is None :
        return Response({'message':'Please Provide the excel file'},status=status.HTTP_400_BAD_REQUEST)
    
    df = pd.read_excel(request.data.get('file'))
    df.apply(addTeachers, axis=1)
    return Response({'message':'Subjects added successfully'},status=status.HTTP_200_OK)
    

def addSubjectDetails(detail):
    subdetail =  SubjectDetail.objects.create(tid = FacultyDetail.objects.get(tid = User.objects.get(uid = detail['tid'])), subject_id = Subject.objects.get(subject_name= detail['subject_name']))
    subdetail.save()


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def subjectDetails(request):
    if request.data.get('file') is None :
        return Response({'message':'Please Provide the excel file'},status=status.HTTP_400_BAD_REQUEST)
    
    df = pd.read_excel(request.data.get('file'))
    df.apply(addSubjectDetails, axis=1)
    return Response({'message':'Subjects added successfully'},status=status.HTTP_200_OK)
    