from django.test import TestCase

# Create your tests here.

# def serialize(self):
#     # print(self.rank.airforce_rank)
#     return {
#         "pk": self.pk,
#         "rank": self.rank.airforce_rank,
#         "first_name_eng": self.first_name_eng,
#         "last_name_eng": self.last_name_eng,
#         "first_name_thai": self.first_name_thai,
#         "last_name_thai": self.last_name_thai,
#         "date_birth": self.date_birth,
#         "line_id": self.line_id,
#         "telephone": self.telephone,
#         "email": self.email,
#         "picture": f'{self.picture}',
#         "division": f'{self.division}',
#         "position": f'{self.position}',
#         "position_other": self.position_other,
#         "lucky_number": self.lucky_number,
#         "afaps": self.afaps,
#         "passport": self.passport,
#         "visa": self.visa,
#         "still_service": self.still_service,
#         "is_pilot": self.is_pilot,
#         "create_at": self.create_at,
#         "update": self.update.strftime("%b %d %Y, %I:%M %p"),
#     }


# storage.py
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import os

# class OverwriteStorage(FileSystemStorage):

#     def get_available_name(self, name):
#         """Returns a filename that's free on the target storage system, and
#         available for new content to be written to.

#         Found at http://djangosnippets.org/snippets/976/

#         This file storage solves overwrite on upload problem. Another
#         proposed solution was to override the save method on the model
#         like so (from https://code.djangoproject.com/ticket/11663):

#         def save(self, *args, **kwargs):
#             try:
#                 this = MyModelName.objects.get(id=self.id)
#                 if this.MyImageFieldName != self.MyImageFieldName:
#                     this.MyImageFieldName.delete()
#             except: pass
#             super(MyModelName, self).save(*args, **kwargs)
#         """
#         # If the filename already exists, remove it as if it was a true file system
#         if self.exists(name):
#             os.remove(os.path.join(settings.MEDIA_ROOT, name))
#         return name

class MyTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

          # set access token in browser with Httponly cookie.
        res = Response(serializer.validated_data, status=status.HTTP_200_OK)
        access_token = serializer.validated_data['access']
        res.set_cookie("access_token", access_token, max_age=settings.SIMPLE_JWT.get(
            'ACCESS_TOKEN_LIFETIME').total_seconds(), samesite='Lax', secure=False, httponly=True)

        return res


# @csrf_exempt
# @permission_classes([IsAuthenticated])
@ensure_csrf_cookie
@api_view(['POST'])
def login_react(request):
    if request.method == "POST":
        data = json.loads(request.body)

        email = data['email']
        password = data['password']

        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)

            response = Response()
            response.set_cookie(key='jwt', value=token,
                                httponly=True, max_age=86400)
            response.data = {
                'message': 'success',
            }
            # return Response({"hey": email})
            return response
        else:
            return Response({"hey": 0})


#in file authenthicate.py
# from rest_framework_simplejwt.authentication import JWTAuthentication    
# from django.conf import settings

# class CookieHandlerJWTAuthentication(JWTAuthentication):
#     def authenticate(self, request):
#         # If cookie contains access token, put it inside authorization header
#         access_token = request.COOKIES.get('access_token')
#         if(access_token):
#             request.META['HTTP_AUTHORIZATION'] = '{header_type} {access_token}'.format(
#                 header_type=settings.SIMPLE_JWT['AUTH_HEADER_TYPES'][0], access_token=access_token)

#         return super().authenticate(request)

# class BlacklistTokenUpdateView(APIView):
#     permission_classes = [AllowAny]
#     authentication_classes = ()

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

@ensure_csrf_cookie
@api_view(['POST'])
def logout_react(request):
    if request.method == 'POST':

        logout(request)
        response = Response()
        response.delete_cookie('access_token')
        response.data = {
            'message': 'Loged out',
        }
        # return Response({"hey": email})
        return response

@login_required
def person(request):
    """ส่งแค่ division ไปเพื่อใช้ในการกด ของ user เอา เพราะถ้าส่งไปหมดจะ load ช้าเกิน """

    # employees = Employee.objects.order_by('afaps')
    divisions = Division.objects.all()

    form = PictureForm()

    context = {
        # 'employees': employees,
        'divisions': divisions,
        'form': form,
    }
    return render(request, "myapp/person.html", context)


# path('person', views.person, name='person'),
@login_required
def pilot_c130(request):
    """แสดงนักบิน C130 ที่ผ่านมาทุกคน """
    # employees = Employee.objects.filter(is_pilot=True).order_by('lucky_number')
    employees = []
    context = {
        'employees': employees,
    }
    return render(request, "myapp/pilot_c130.html", context)

# def open_access_middleware(get_response):
#     def middleware(request):
#         response = get_response(request)
#         response["Access-Control-Allow-Origin"] = "http://localhost:3000"
#         response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
#         response["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept, Authorization, x-csrftoken"
#         return response
#     return middleware

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer', 'JWT'),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}