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
from faculty.models import FacultyDetail, Subject, SubjectDetail
from students.models import StudentDetail
# Create your views here.

User=get_user_model()

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def LoginView(request):
    
    data=request.data
    uid=data.get('uid')
    password=data.get('password')
    role=int(data.get('role'))
    if (uid is None or password is None or role is None):
        return Response({'message':'Provide All the Details'},status=status.HTTP_400_BAD_REQUEST)
    
    user = auth.authenticate(uid=uid,password=password)
    print('user: ',user)
    if user:
        if role == user.role:
            token = get_tokens_for_user(user)
            if role == 1:
                teacher = FacultyDetail.objects.get(tid = user)
                data={
                    'token': token,
                    'uid': user.uid,
                    'name': teacher.name,
                    'department': teacher.department,
                    'email': teacher.email
                }
            elif role == 2:
                student = StudentDetail.objects.get(sid = user)
                data={
                    'token': token,
                    'uid': user.uid,
                    'name': student.name,
                    'email': student.email,
                    'course': student.course,
                    'semester': student.semester,
                    'university_roll_no': str(student.university_roll_no),
                }
            else:
                data={
                    'token': token,
                    'uid': user.uid,
                }
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({'message':'Invalid user'},status=status.HTTP_401_UNAUTHORIZED)
    return Response({'message':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)

def random_id():
    id = int(''.join(secrets.choice(string.digits)for i in range(6)))
    return id

@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def send_otp(request):
    user=User.objects.get(uid=request.data.get('uid'))
    if user is not None:
        email_otp=random_id()
        subject = 'Change Password'
        message = f"Welcome to Hansraj College !\n Your otp is {email_otp}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        #send_mail(subject, message, email_from, recipient_list, fail_silently=True)
        email = EmailMessage(
                    subject,
                    message,
                    email_from,
                    recipient_list,)
        email_count = email.send(fail_silently=False)
        print(email_count)
        user.otp=email_otp
        user.save()
        return Response({'message':'Mail sent'},status=status.HTTP_200_OK)
    else:
        return Response({'message':'Invalid UserID(uid)'},status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def otp_verification(request):
    user=User.objects.get(uid=request.data.get('uid'))
    if user is not None:
        if user.otp == int(request.data.get('otp')):
            user.otp = None
            user.save()
            return Response({'message':'OTP Verified'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'Invalid OTP'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'Invalid UserID(uid)'},status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def forget_password(request):
    user=User.objects.get(uid=request.data.get('uid'))
    print(user.password)
    if user is not None:
        if request.data.get('new_password') == request.data.get('confirm_password'):
            user.set_password(request.data.get('new_password'))
            user.save()
            return Response({'message':'Password changed successful'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'Password not matching'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'Invalid UserID(uid)'},status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def change_password(request):
    user=User.objects.get(uid=request.user.uid)
    print(user.password)
    if user is not None:
        if user.check_password(request.data.get('old_password')):
            if request.data.get('new_password') == request.data.get('confirm_password'):
                user.set_password(request.data.get('new_password'))
                user.save()
                return Response({'message':'Password changed successful'},status=status.HTTP_200_OK)
            else:
                return Response({'message':'Password not matching'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'Invalid Old Password'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'Invalid UserID(uid)'},status=status.HTTP_400_BAD_REQUEST)



def createuser(newuser):
    try:
        print(newuser)
        user=  User.objects.create_user(uid= newuser['uid'], password = str(newuser['password']), role = newuser['role'], email = newuser['email'])
        user.save()
    except:
        return newuser['uid']
    


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
@user_passes_test(lambda u: not u.is_authenticated)
def addUsers(request):
    if request.data.get('file') is None :
        return Response({'message':'Please Provide the excel file'},status=status.HTTP_400_BAD_REQUEST)
    
    df = pd.read_excel(request.data.get('file'))
    for i in df.index:
        x = createuser(df.iloc[i])
        if x is not None:
            return Response({'message': 'User with uid {} already exist!'.format(x)}, status = status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Users added successfully'},status=status.HTTP_200_OK)
    

@api_view(["POST"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def logout_user(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({'message':'Users logged out successfully!'}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'message':'Error logging user out!'}, status=status.HTTP_400_BAD_REQUEST)
