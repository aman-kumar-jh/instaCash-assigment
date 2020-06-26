from django.urls import path

from .views import (
    
    TaskView,
    TodayTaskList,
    TaskCreateView,
    TaskDetailView,
    TaskDeleteView,
    TaskUpdateView,
    CompleteTask,
    
)

urlpatterns = [
    path('', TaskView, name='task_list'),
    path('now/', TodayTaskList, name='today_task_list'),
    
    path('new/', TaskCreateView.as_view(), name='task_new'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    
    path('<int:pk>/complete', CompleteTask, name='task_complete'),
]