from rest_framework import authentication, exceptions
import jwt
from django.conf import settings
from users.models import User


class PortalAuthentication(authentication.BaseAuthentication):

    ## To fetch the bearer Token
    def get_jwt_token(self, request):
        auth = authentication.get_authorization_header(
            request).split()

        if not auth or auth[0].lower() != b'bearer':
            msg = ('Invalid auth header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        
        if len(auth) == 1:
            msg = ('Invalid auth header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = ('Invalid auth header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        return auth[1]

    def validate_jwt(self, token):
        try:
            decoded_jwt = jwt.decode(
                token,settings.SECRET_KEY,
                verify=True,
                algorithms=['HS256'],
                )
            return decoded_jwt
        except jwt.exceptions.InvalidAudienceError:
            msg = ('Invalid audience')
        except jwt.exceptions.InvalidIssuerError:
            msg = ('Invalid issuer')
        except jwt.exceptions.ExpiredSignatureError:
            msg = ('Expired signature')
        except jwt.exceptions.ImmatureSignatureError:
            msg = ('Immature signature')
        except jwt.exceptions.InvalidSignatureError:
            msg = ('Invalid signature') 
        except Exception as e:
            print("Unknown error occured in validate_jwt",e)
            msg = ('Invalid token')   
        raise exceptions.AuthenticationFailed(msg)


    def authenticate(self, request):
        token = self.get_jwt_token(request)
        if not token:
            return None
        decoded_jwt = self.validate_jwt(token)
        uid = decoded_jwt['uid']

        try:
            user=User.objects.get(uid=uid)
        except:
            print("User Does Not Exists")
            raise exceptions.AuthenticationFailed("User Does Not Exists")
        
        request.user=user
        return user