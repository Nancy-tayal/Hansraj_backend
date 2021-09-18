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
    role=data.get('role')
    user = auth.authenticate(uid=uid,password=password)
    print('user: ',user)
    if user:
        if int(role) == user.role:
            token = get_tokens_for_user(user)
            data={
                'token':token,
                'uid':user.uid,
                'role':user.role,
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response({'detail':'Invalid user'},status=status.HTTP_401_UNAUTHORIZED)
    return Response({'detail':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)

@api_view(["POST"])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def change_password(request):
    if request.user.role == 0 :
        user=User.objects.get(uid=request.data.get('uid'))
        if user is not None:
            user.set_password(request.data.get('password'))
            user.save()
        else:
            return Response({'detail':'Invalid UserID(uid)'},status=status.HTTP_400_BAD_REQUEST)
    else:
            return Response({'detail':'Invalid user. User should be Admin.'},status=status.HTTP_400_BAD_REQUEST)

