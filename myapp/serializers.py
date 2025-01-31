from rest_framework import serializers
from .models import*



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','user', 't_name', 'address', 'phone', 'role']

class SubjectSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.t_name', read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'subject_name', 'teacher', 'teacher_name']

class ClassroomSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = ClassLevel
        fields = ['id', 'name', 'subjects'] 

class AttendanceSerializer(serializers.ModelSerializer):
     student_name = serializers.CharField(source='student.name', read_only=True)
     classroom_name = serializers.CharField(source='classroom.name', read_only=True)
     subject_name = serializers.CharField(source='subject.subject', read_only=True)

     class Meta:
        model = Attendance
        fields = ['id','student', 'student_name', 'classroom', 'classroom_name', 'subject', 'subject_name', 'date', 'reason', 'status']

