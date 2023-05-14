from django.conf.urls.static import static
from django.urls import path

from internship_01052023 import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    path('add_task/', views.add_task, name='add_task'),
    path('task_list/', views.task_list, name='task_list'),
    path('task_detail/<int:pk>/', views.task_detail, name='task_detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
