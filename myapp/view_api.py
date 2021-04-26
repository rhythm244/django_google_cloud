from django.contrib.auth import authenticate, login, logout
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from django.http import JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import ensure_csrf_cookie
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
@ensure_csrf_cookie
# @permission_classes([IsAuthenticated])
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
            return Response({"hey": email})
        else:
            return Response({"hey": 0})

#use Token for authorize
@api_view(['GET', 'PUT'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @authentication_classes([JSONWebTokenAuthentication,])
#บรรทัดบนคือ ถ้าใส่แล้วถ้ามี session มันจะไม่ขออีกที แต่ต้องอ่าน DOC อีกเยอะคร่าวๆใส่ Token ทุกครั้งไปจบ
@permission_classes([IsAuthenticated])
def api_employees(request):
    if request.method == 'GET':
        employee = Employee.objects.all().filter(is_pilot=True).order_by('lucky_number')
        serializer = EmployeeSerializer(employee, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response({"hey" : "Hello Thong"})

    #ยังไม่ได้เทส 19/04/2021 ,0747
    elif request.method == 'PUT':
        employee = Employee.objects.all().filter(is_pilot=True).order_by('lucky_number')
        serializer = EmployeeSerializer(employee, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)