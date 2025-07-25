from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage, TaskReorder 

from .views import logout_view

from . import views

    




urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('logout/', logout_view, name='logout'),

    path('register/', RegisterPage.as_view(), name='register'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle-complete'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]