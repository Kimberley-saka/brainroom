"""
URLs
"""
from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.get_courses),
    path('courses/<int:id>/', views.get_specific_course),
    path('courses/<int:course_id>/lessons/', views.get_lessons),
    path('lessons/<int:id>/', views.get_specific_lesson),
    path('instructor/courses/add/', views.add_course),
    path('instructor/courses/update/', views.update_course),
    path('instructor/lessons/add/', views.add_lesson),
    path('instructor/lessons/update/', views.update_lesson),
    path('user/<int:user_id>/lessons/<lesson_id>/complete/', views.add_progress),
    path('user/<int:user_id>/progress/', views.get_progress)
]
