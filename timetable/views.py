from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes,api_view
import pandas as pd
from .models import Timetable
from students.models import StudentDetail
from django.http import HttpResponse
from django.forms.models import model_to_dict
from faculty.models import SubjectDetail
# Create your views here.

User = get_user_model()

@api_view(["POST"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def timetable(request):
    student = StudentDetail.objects.get(sid= request.user)
    day = request.data.get('day')
    if day is None:
        return Response({"message": "Please provide the day!"}, status= status.HTTP_400_BAD_REQUEST)
    if student is not None:
        table = Timetable.objects.get_or_none(course = student.course, semester = student.semester, day = day)
        if table is None:
            return Response({'message':'No data available!'}, status= status.HTTP_200_OK)
        table = {key: getattr(table, key) for key in model_to_dict(table).keys()} 
        time = ['8:40 - 9:40', '9:40 - 10:40', '10:40 - 11:40', '11:40 - 12:40', '1:00 - 2:00', '2:40 - 3:00', '3:00 - 4:00', '4:00 - 5:00' ]
        x = list()
        j = 0
        for i in table:
            if i != 'id' and i != 'course' and i !='semester' and i!='day':
                y = dict()
                if table[i] is not None:
                    y['time'] = time[j]
                    y['subject'] = table[i].subject_name
                    subject = SubjectDetail.objects.filter(subject_id = table[i])
                    st = list()
                    for sub in subject:
                        st.append(sub.tid.name) 
                    y['teachers'] = ', '.join(st)
                    x.append(y)
                else:
                    y['time'] = time[j]
                    y['subject'] = None
                    y['teachers'] = None
                    x.append(y)
                j += 1
        return Response(x, status = status.HTTP_200_OK)        
    else:
        return Response({'message':'Student Does Not Exist!'},status=status.HTTP_400_BAD_REQUEST)
