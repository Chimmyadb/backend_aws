from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Custom User model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('teacher', 'teacher'),
        
         
        
    ]
    username=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    roups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Avoid clashes with the default User model
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Avoid clashes with the default User model
        blank=True,
    )
# Student model
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=1,choices=[('M','Male'),('F','Female')])
    address=models.TextField()
    guardian_name=models.CharField(max_length=100)
    guardian_phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

# Teacher model
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    t_name=models.CharField(max_length=50)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, default='teacher')


    def __str__(self):
        return self.t_name

# Subject model
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.subject_name

# Class model
class ClassLevel(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, related_name="classes")

    def __str__(self):
        return self.name

# Attendance model
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    reason=models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.status} on {self.date}"
    


