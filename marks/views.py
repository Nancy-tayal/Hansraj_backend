import json
from django.db.models import F
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes,api_view
import pandas as pd
from faculty.models import SubjectDetail, Subject, FacultyDetail
from students.models import StudentDetail
from .models import Marks_Out_Of, Marks
from django.http import JsonResponse
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
        data = request.data.get('data')
        if subject_id is None or field is None or total_marks is None or data is None:
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
            
            data = json.loads(data)
            df = pd.json_normalize(data)
            print(df)
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

@api_view(["POST"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def studentsMarks(request):
    teacher = FacultyDetail.objects.get(tid= request.user)
    subject = request.data.get('subject_id')
    field = request.data.get('field')
    if teacher is not None :
        if subject is None or field is None:
            return Response({'message':'Please provide all the details!'},status=status.HTTP_400_BAD_REQUEST)
        subject_id = Subject.objects.get_or_none(subject_id = subject)
        if subject_id is None:
            return Response({'message':'Invalid Subject ID!'},status=status.HTTP_400_BAD_REQUEST)
        detail_id = SubjectDetail.objects.get_or_none(tid = teacher, subject_id = subject_id)
        total = Marks_Out_Of.objects.get_or_none(detail_id = detail_id)
        total = total.__dict__
        stud_marks = Marks.objects.filter(detail_id = detail_id).values(RollNo =F('sid__sid__uid'), Name =F('sid__name') , course= F('sid__course'),Marks = F(field)).order_by('sid__sid__uid')
        x = list(stud_marks)
        y = {}
        y['total_marks']= total[field]
        x.insert(0,y)
        return JsonResponse(x,status=status.HTTP_200_OK, safe=False)
    else:
        return Response({'message':'Teacher Does Not Exist!'},status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def getMarks(request):
    if request.data.get('detail_id') is None :
        return Response({'message':'Please Provide the detail_id'},status=status.HTTP_400_BAD_REQUEST)
    elif request.data.get('field') is None :
        return Response({'message':'Please Provide the field(assignment or internal'},status=status.HTTP_400_BAD_REQUEST)
    else :
        student = StudentDetail.objects.get(sid= request.user)
        if student is not None :
            x = list()
            marks = Marks.objects.get_or_none(sid = student, detail_id = request.data.get('detail_id'))
            if marks is not None:
                if request.data.get('field') == 'assignment':
                    assignment_marks = Marks.objects.filter(detail_id = request.data.get('detail_id'), sid = student).values('a1','a2','a3','a4','a5','a6','a7','a8','a9','a10')
                    assignment_marks = list(assignment_marks)[0]
                    assignment_out_of = Marks_Out_Of.objects.filter(detail_id = request.data.get('detail_id')).values('a1','a2','a3','a4','a5','a6','a7','a8','a9','a10')
                    assignment_out_of = list(assignment_out_of)[0]
                    for i in range(1,11):
                        y = dict()
                        if assignment_out_of['a'+ str(i)] is None:
                            del assignment_marks['a'+str(i)]
                            del assignment_out_of['a'+str(i)]
                        else:
                            y['type'] = 'a'+str(i)
                            y['marks'] = assignment_marks['a'+str(i)]
                            y['out_of'] = assignment_out_of['a'+str(i)]
                            x.append(y)
                elif request.data.get('field') == 'internal':
                    internal_marks = Marks.objects.filter(detail_id = request.data.get('detail_id')).values('i1','i2','i3')
                    internal_marks = list(internal_marks)[0]
                    internal_out_of = Marks_Out_Of.objects.filter(detail_id = request.data.get('detail_id')).values('i1','i2','i3')
                    internal_out_of = list(internal_out_of)[0]
                    for i in range(1,4):
                        y = dict()
                        if internal_marks['i'+str(i)] is None:
                            del internal_marks['i'+str(i)]
                            del internal_out_of['i'+str(i)]
                        else:
                            y['type'] = 'i'+str(i)
                            y['marks'] = internal_marks['i'+str(i)]
                            y['out_of'] = internal_out_of['i'+str(i)]
                            x.append(y)
                return Response(x,status=status.HTTP_200_OK)
            else:
                return Response({'message':'Marks does not exist!'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'Student does not exist!'},status=status.HTTP_400_BAD_REQUEST)