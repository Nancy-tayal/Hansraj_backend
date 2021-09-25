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
from .models import StudentDetail
from faculty.models import Subject
# Create your views here.

User = get_user_model()

def addStudentDetails(student):
    #detail =  StudentDetail.objects.create(sid= User.objects.get(uid=student['sid']), name = student['name'], email = student['email'], university_roll_no = student['university_roll_no'], semester = student['semester'])
    #detail.course = student['course']
    #print(detail.course)
    #detail.save()
    print('xyz', len(student['course']))

@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def studentdetails(request):
    if request.data.get('file') is None :
        return Response({'message':'Please Provide the excel file'},status=status.HTTP_400_BAD_REQUEST)
    
    df = pd.read_excel(request.data.get('file'))
    df.apply(addStudentDetails, axis=1)
    return Response({'message':'Student Details added successfully'},status=status.HTTP_200_OK)
    