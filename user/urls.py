from django.urls import path
from .views import UserProfilAPIview, TaskAPIView,UserProfileDetailView, TaskListCreateView, TaskDetailView, TaskByStatusView, OverdueTasksView


urlpatterns = [
    path('api/profile/', UserProfilAPIview.as_view(), name='profile'),
    path('api/tasks/', TaskAPIView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskAPIView.as_view(), name='task-detail'),    
    path('<int:pk>/', UserProfilAPIview.as_view()),
    path('profile/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/status/<str:status>/', TaskByStatusView.as_view(), name='tasks-by-status'),
    path('tasks/overdue/', OverdueTasksView.as_view(), name='overdue-tasks'),
]