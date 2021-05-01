import json

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Employee
from .serializers import EmployeeSerializer

# from django.views.decorators.csrf import csrf_exempt


# use Token for authorize
@api_view(['GET', 'PUT'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @authentication_classes([JSONWebTokenAuthentication,])
# บรรทัดบนคือ ถ้าใส่แล้วถ้ามี session มันจะไม่ขออีกที แต่ต้องอ่าน DOC อีกเยอะคร่าวๆใส่ Token ทุกครั้งไปจบ
# @permission_classes([IsAuthenticated])
def api_employees(request):
    if request.method == 'GET':
        employee = Employee.objects.all().filter(
            is_pilot=True).order_by('lucky_number')
        serializer = EmployeeSerializer(employee, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response({"hey": "Hello Thong"})

    # ยังไม่ได้เทส 19/04/2021 ,0747
    elif request.method == 'PUT':
        employee = Employee.objects.all().filter(
            is_pilot=True).order_by('lucky_number')

        serializer = EmployeeSerializer(employee, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
