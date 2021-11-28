from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from rest_framework.response import Response
from clients.serializers import UserRegisterSerializer,clienttokenauthenticationSerializer
from clients.models import User_Register,client_token_authentication

from . import permissions

class profile(viewsets.ViewSet):
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request):
        #phone = request.GET.get('phone',None)
        user= User_Register.objects.all()
        serialized_user = UserRegisterSerializer(user,many=True)
        return Response({'user': serialized_user.data })



#--------------------------------------------------
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
#from django.views.decorators.csrf import ensure_csrf_cookie
from auth_travel.utils import generate_access_token, generate_refresh_token

@api_view(['GET'])
@permission_classes([AllowAny])
#@ensure_csrf_cookie
def login_view(request):
    phone_number=request.GET.get('phone_number')

    if (phone_number is None):
        raise exceptions.AuthenticationFailed(' Phone Number required')



    user_inst=User_Register.objects.filter(mobile=phone_number)
    user= client_token_authentication.objects.filter(user_phonenumber=phone_number)

    if len(user_inst)==0 or len(user)==0:
        raise exceptions.AuthenticationFailed('user not found views')





    serialized_user=clienttokenauthenticationSerializer(user,many=True)
    for usr in user:
        email=usr.user_email
        phone_number=usr.user_phonenumber

    access_token=generate_access_token(user_inst)
    refresh_token=generate_refresh_token(user_inst)

    # Here stored in DB

    return Response({
        'access_token':access_token,
        'refresh_token':refresh_token,
        'email':email,
        'phone_number':phone_number
    })