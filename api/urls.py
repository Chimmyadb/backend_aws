
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import api_view
from myapp.views import*
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # For logging in
    TokenRefreshView,     # For refreshing the JWT token
)

urlpatterns = [

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token
   
    path('students/', manage_student, name='get_students'),  
    path('student/<int:id>/', manage_student, name='get_student'),

    path('teachers/', manage_teacher, name='get_teachers'),  
    path('teacher/<int:id>/', manage_teacher, name='get_teacher'), 

    path('subjects/', manage_subject, name='get_subject'),
    path('subject/<int:id>/', manage_subject, name='get_subject'),

    path('classrooms/', manage_classroom, name='get_classroom'),
    path('classroom/<int:id>/', manage_classroom, name='get_classroom'),

    path('attendances/', manage_attendance, name='get_attendances'),
    path('attendance/<int:id>/', manage_attendance, name='get_attendance'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


