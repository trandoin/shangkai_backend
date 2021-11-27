import jwt
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions
from django.conf import settings
from clients.models import User_Register #client_token_authentication


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Return the failure reason instead of an HttpResponse
        return reason

class SafeJWTAuthentication(BaseAuthentication):


    def authenticate(self,request):
        authorization_heaader=request.headers.get('Authorization')

        if not authorization_heaader:
            return None
        try:
            access_token=authorization_heaader.split(' ')[1]
            payload=jwt.decode(access_token,settings.SECRET_KEY,algorithms=['HS256'])



        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')
        except:
            raise exceptions.AuthenticationFailed('Invalid Token')


        user=user_token_authentication.objects.filter(user=payload['id']).first()
        user_inst=user_details.objects.filter(id=payload['id']).first()
        if (user is None) or (user_inst is None):
            raise exceptions.AuthenticationFailed('user not found')


        return (user_inst, None)

    """
    def authenticate_credentials(self, token):
        payload=jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
        email = payload['id']
        msg = {'Error': "Token mismatch",'status' :"401"}
        try:
            user=user_token_authentication.objects.get(user_email=email)
            if user.accessToken==token:
                raise exceptions.AuthenticationFailed(msg)


        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return HttpResponse({'Error': "Token is invalid"}, status="403")
        except User.DoesNotExist:
            return HttpResponse({'Error': "Internal server error"}, status="500")

        return (user, token)
    """

    def authenticate_header(self, request):
        return 'Token'




