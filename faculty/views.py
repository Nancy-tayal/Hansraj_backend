from os import stat
from re import S, sub
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
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.conf import settings
import secrets
import string
import pandas as pd
from .models import SubjectDetail, Subject, FacultyDetail
from attendance.models import Attendance_Out_Of
from students.models import StudentDetail
from marks.models import Marks_Out_Of
from .serializers import SubjectsListSerializer, StudentsListSerializer
# Create your views here.
User = get_user_model()


def addSubjects(subj):

    subject = Subject.objects.get_or_none(subject_name = subj['subject_name'])
    if subject is None:
        subject =  Subject.objects.create(subject_name = subj['subject_name'])
        subject.save()
    else:
        return subj['subject_name']


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def subjects(request):
    if request.data.get('file') is None :
        return Response({'message':'Please Provide the excel file'},status=status.HTTP_400_BAD_REQUEST)
    
    df = pd.read_excel(request.data.get('file'))
    for i in df.index:
        x = addSubjects(df.iloc[i])
        if x is not None:
            return Response({'message': 'Subject {} already exist!'.format(x)}, status = status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Subjects added successfully'},status=status.HTTP_200_OK)
    


def addTeachers(teacher):
    faculty = ''
    try:
        faculty =  FacultyDetail.objects.create(tid = User.objects.get(uid = teacher['tid']), name = teacher['name'], email = teacher['email'], department = teacher['department'])
        faculty.save()
    except ObjectDoesNotExist:
        return -1
    except:
        return teacher['tid']


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def teachers(request):
    if request.data.get('file') is None :
        return Response({'message':'Please Provide the excel file'},status=status.HTTP_400_BAD_REQUEST)
    
    df = pd.read_excel(request.data.get('file'))
    for i in df.index:
        x = addTeachers(df.iloc[i])
        if x is not None:
            if x != -1:
                return Response({'message': 'Teacher with tid {} already exist!'.format(x)}, status = status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Teacher with tid {} has no occurence in the login table! Please get the teacher registered first!'.format(df.iloc[i]['tid'])}, status = status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Teachers added successfully'},status=status.HTTP_200_OK)
    

def addSubjectDetails(detail):
    try:
        tid = FacultyDetail.objects.get(tid = User.objects.get(uid = detail['tid']))
        subject_id = Subject.objects.get(subject_name= detail['subject_name'])
    except ObjectDoesNotExist:
        return -2
    subdetail =  SubjectDetail.objects.get_or_none(tid = tid,  subject_id = subject_id)
    if subdetail is None:
            subdetail =  SubjectDetail.objects.create(tid = tid,  subject_id = subject_id)
            subdetail.save()
    else:
        return -1

@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def subjectDetails(request):
    if request.data.get('file') is None :
        return Response({'message':'Please Provide the excel file'},status=status.HTTP_400_BAD_REQUEST)
    
    df = pd.read_excel(request.data.get('file'))
    for i in df.index:
        x = addSubjectDetails(df.iloc[i])
        if x is not None:
            if x == -2:
                return Response({'message': 'Either Teacher with tid {0} or Subject with subject name {1} does not exist!'.format(df.iloc[i]['tid'],df.iloc[i]['subject_name'])}, status = status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Subject Detail with tid {0} and subject name {1} already exist!'.format(df.iloc[i]['tid'],df.iloc[i]['subject_name'])}, status = status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Subjects added successfully'},status=status.HTTP_200_OK)
    


@api_view(["GET"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def subjectsList(request):
    teacher = FacultyDetail.objects.get(tid= request.user)
    if teacher is not None:
        subjectdetails = SubjectDetail.objects.filter(tid = teacher)
        serialized_data = SubjectsListSerializer(subjectdetails, many=True)
        return Response(serialized_data.data,status=status.HTTP_200_OK)
    else:
        return Response({'message':'Teacher Does Not Exist!'},status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def studentsAttendanceList(request):
    teacher = FacultyDetail.objects.get(tid= request.user)
    if teacher is not None:
        subject_id = request.data.get('subject_id')
        month = request.data.get('month')
        total_lectures = int(request.data.get('total_lectures'))
        if subject_id is None or month is None or total_lectures is None:
            return Response({'message':'Provide all the details!'},status=status.HTTP_400_BAD_REQUEST)
        else:
            detail_id = SubjectDetail.objects.get(tid = teacher, subject_id = Subject.objects.get(subject_id = subject_id))
            attendance = Attendance_Out_Of.objects.get_or_none(detail_id = detail_id)
            if attendance is None:
                attendance = Attendance_Out_Of.objects.create(**{month : total_lectures, 'detail_id' : detail_id})
            else:
                setattr(attendance, month, total_lectures) 
            attendance.total = attendance.m1 + attendance.m2 + attendance.m3 + attendance.m4 + attendance.m5 + attendance.m6 + attendance.m7 + attendance.m8 + attendance.m9 + attendance.m10 + attendance.m11 + attendance.m12   
            attendance.save()

            subjectdetails = StudentDetail.objects.filter(subject = SubjectDetail.objects.get(tid = teacher, subject_id = Subject.objects.get(subject_id = subject_id)))
            serialized_data = StudentsListSerializer(subjectdetails, many=True)
            return Response(serialized_data.data,status=status.HTTP_200_OK)                 
    else:
        return Response({'message':'Teacher Does Not Exist!'},status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def studentsMarksList(request):
    teacher = FacultyDetail.objects.get(tid= request.user)
    if teacher is not None:
        subject_id = request.data.get('subject_id')
        field = request.data.get('field')
        total_marks = int(request.data.get('total_marks'))
        if subject_id is None or field is None or total_marks is None:
            return Response({'message':'Provide all the details!'},status=status.HTTP_400_BAD_REQUEST)
        else:
            detail_id = SubjectDetail.objects.get(tid = teacher, subject_id = Subject.objects.get(subject_id = subject_id))
            print(detail_id)
            marks = Marks_Out_Of.objects.get_or_none(detail_id = detail_id)
            if marks is None:
                marks = Marks_Out_Of.objects.create(**{field : total_marks, 'detail_id' : detail_id})
            else:
                setattr(marks, field, total_marks)
            marks.save()

            subjectdetails = StudentDetail.objects.filter(subject = SubjectDetail.objects.get(tid = teacher, subject_id = Subject.objects.get(subject_id = subject_id)))
            serialized_data = StudentsListSerializer(subjectdetails, many=True)
            return Response(serialized_data.data,status=status.HTTP_200_OK)                 
    else:
        return Response({'message':'Teacher Does Not Exist!'},status=status.HTTP_400_BAD_REQUEST)
