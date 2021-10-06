from django.db.models import F
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes,api_view
import pandas as pd
from faculty.models import SubjectDetail, Subject, FacultyDetail
from .models import Attendance_Out_Of, Attendance
from students.models import StudentDetail
from django.http import JsonResponse
# Create your views here.
User = get_user_model()



@api_view(["POST"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def uploadAttendance(request):
    teacher = FacultyDetail.objects.get(tid= request.user)
    if teacher is not None:
        subject_id = request.data.get('subject_id')
        month = request.data.get('month')
        total_lectures = int(request.data.get('total_lectures'))
        file = request.data.get('file')
        if subject_id is None or month is None or total_lectures is None or file is None:
            return Response({'message':'Provide all the details!'},status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                detail_id = SubjectDetail.objects.get(tid = teacher, subject_id = Subject.objects.get(subject_id = subject_id))
            except:
                return Response({'message':'There is no record for the selected subject being taught by {}!'.format(teacher.name)},status=status.HTTP_400_BAD_REQUEST)
            
            attendance = Attendance_Out_Of.objects.get_or_none(detail_id = detail_id)
            if attendance is None:
                attendance = Attendance_Out_Of.objects.create(**{month : total_lectures, 'detail_id' : detail_id})
            else:
                setattr(attendance, month, total_lectures) 
            attendance.total = attendance.m1 + attendance.m2 + attendance.m3 + attendance.m4 + attendance.m5 + attendance.m6 + attendance.m7 + attendance.m8 + attendance.m9 + attendance.m10 + attendance.m11 + attendance.m12   
            attendance.save()

            try:
                df = pd.read_excel(file)
            except:
                return Response({'message':'Incorrect File Format!'},status=status.HTTP_400_BAD_REQUEST)
            for i in df.index:
                sid = StudentDetail.objects.get(sid = User.objects.get(uid=df.iloc[i]['sid']))
                stud_attendance = Attendance.objects.get_or_none(detail_id = detail_id, sid = sid )
                if stud_attendance is None:
                    stud_attendance = Attendance.objects.create(**{month : df.iloc[i]['attendance'], 'detail_id' : detail_id, 'sid' : sid })
                else:
                    setattr(stud_attendance, month, df.iloc[i]['attendance']) 
                
                stud_attendance.total = stud_attendance.m1 + stud_attendance.m2 + stud_attendance.m3 + stud_attendance.m4 + stud_attendance.m5 + stud_attendance.m6 + stud_attendance.m7 + stud_attendance.m8 + stud_attendance.m9 + stud_attendance.m10 + stud_attendance.m11 + stud_attendance.m12   
                stud_attendance.save()

            return Response({'message':'Students Attendance Uploaded Successfully!'},status=status.HTTP_200_OK)

    else:
        return Response({'message':'Teacher Does Not Exist!'},status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def studentsAttendance(request):
    teacher = FacultyDetail.objects.get(tid= request.user)
    subject = request.data.get('subject_id')
    month = request.data.get('month')
    if teacher is not None :
        if subject is None or month is None:
            return Response({'message':'Please provide all the details!'},status=status.HTTP_400_BAD_REQUEST)
        subject_id = Subject.objects.get_or_none(subject_id = subject)
        if subject_id is None:
            return Response({'message':'Invalid Subject ID!'},status=status.HTTP_400_BAD_REQUEST)
        detail_id = SubjectDetail.objects.get_or_none(tid = teacher, subject_id = subject_id)
        total = Attendance_Out_Of.objects.get_or_none(detail_id = detail_id)
        total = total.__dict__
        studentsattendance = Attendance.objects.filter(detail_id = detail_id).values(RollNo =F('sid__sid__uid'), Name =F('sid__name') , Attendance = F(month)).order_by('sid__sid__uid')
        x = list(studentsattendance)
        y = {}
        y['total_attendance'] = total[month]
        x.insert(0, y)
        return JsonResponse(x,status=status.HTTP_200_OK, safe=False)
    else:
        return Response({'message':'Teacher Does Not Exist!'},status=status.HTTP_400_BAD_REQUEST)


