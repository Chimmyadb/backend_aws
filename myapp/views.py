from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from .models import Student
from django.http import JsonResponse
from django.views import View
from .serializers import*
from rest_framework import viewsets
import json
import logging
logger= logging.getLogger(__name__)

# Login view for authentication
class LoginView(View):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            token = RefreshToken.for_user(user)
            return Response({'access': str(token.access_token)})
        return Response({'message': 'Invalid credentials'}, status=400)


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset=ClassLevel.objects.all()
    serializer_class=ClassroomSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset=Attendance.objects.select_related('subject', 'student', 'classroom').all()
    serializer_class=AttendanceSerializer

class SignUpView(View):
    def post(self, request, *args, **kwargs):
        # Your signup logic here
        return JsonResponse({'message': 'User created successfully'}, status=201)
    
@permission_classes([IsAuthenticated])
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'PUT','DELETE'])
    def api(request, id=None):
        logger.debug(f"Request Method: {request.method}, Data: {request.data}")
        #for GET
        if request.method == 'GET':
            if id:
                try:
                    instance=model_class.objects.get(id=id)
                    serializer= serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'object not found'},status=404)
            else:
                instances=model_class.objects.all()
                serializer=serializer_class(instances, many=True)
                return Response(serializer.data)
         #for Insert   
        elif request.method == 'POST':
            serializer=serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        #for Update
        elif request.method == 'PUT':
            if id:
                try:
                    instance=model_class.objects.get(id=id)
                    serializer=serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors, status=400)
                except model_class.DoesNotExist:
                    return JsonResponse({'message': 'object not found'},status=404)
            return Response({'message': 'id is required for update'}, status=400)
        # for Delete
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'}, status=204)
                except model_class.DoesNotExist:
                    return JsonResponse({'message': 'Object not found'}, status=404)
            return Response({'message': 'ID is required for deletion'}, status=400)

        return JsonResponse({'message': 'Invalid method'}, status=405)

    return api

# API views for Student record system
manage_student = generic_api(Student, StudentSerializer)
manage_teacher = generic_api(Teacher, TeacherSerializer)
manage_subject = generic_api(Subject, SubjectSerializer)    
manage_classroom = generic_api(ClassLevel, ClassroomSerializer)    
manage_attendance = generic_api(Attendance, AttendanceSerializer)    

