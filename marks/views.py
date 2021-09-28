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
from faculty.models import SubjectDetail, Subject, FacultyDetail
from students.models import StudentDetail
from .models import Marks_Out_Of, Marks
# Create your views here.

User = get_user_model()


@api_view(["POST"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def uploadMarks(request):
    teacher = FacultyDetail.objects.get(tid= request.user)
    if teacher is not None:
        subject_id = request.data.get('subject_id')
        field = request.data.get('field')
        total_marks = int(request.data.get('total_marks'))
        file = request.data.get('file')
        if subject_id is None or field is None or total_marks is None or file is None:
            return Response({'message':'Provide all the details!'},status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                detail_id = SubjectDetail.objects.get(tid = teacher, subject_id = Subject.objects.get(subject_id = subject_id))
            except:
                return Response({'message':'There is no record for the selected subject being taught by {}!'.format(teacher.name)},status=status.HTTP_400_BAD_REQUEST)
            
            marks = Marks_Out_Of.objects.get_or_none(detail_id = detail_id)
            if marks is None:
                marks = Marks_Out_Of.objects.create(**{field : total_marks, 'detail_id' : detail_id})
            else:
                print('hi')
                setattr(marks, field, total_marks) 
            marks.save()
            df = pd.read_excel(file)
            for i in df.index:
                sid = StudentDetail.objects.get(sid = User.objects.get(uid=df.iloc[i]['sid']))
                stud_marks = Marks.objects.get_or_none(detail_id = detail_id, sid = sid )
                if stud_marks is None:
                    stud_marks = Marks.objects.create(**{field : df.iloc[i]['marks'], 'detail_id' : detail_id, 'sid' : sid })
                else:
                    setattr(stud_marks, field, df.iloc[i]['marks']) 
                stud_marks.save()                
            
            return Response({'message':'Students Marks Uploaded Successfully!'},status=status.HTTP_200_OK)

    else:
        return Response({'message':'Teacher Does Not Exist!'},status=status.HTTP_400_BAD_REQUEST)

