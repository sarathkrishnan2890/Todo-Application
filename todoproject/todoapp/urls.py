from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import CustomLoginView, Taskcreate, RegisterPage, Tasklist, TaskDetailView, TaskUpdate, TaskDelete

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('create/', Taskcreate.as_view(), name='createtask'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('tasklist/', Tasklist.as_view(), name='task'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('task-details/<int:pk>/', TaskDetailView.as_view(), name='details'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
    path('task/delete/<int:pk>/', views.TaskDelete.as_view(), name='delete_task'),
]
