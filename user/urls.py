from django.urls import path
from .views import UserProfilAPIview, TaskAPIView


urlpatterns = [
    path('api/profile/', UserProfilAPIview.as_view(), name='profile'),
    path('api/tasks/', TaskAPIView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskAPIView.as_view(), name='task-detail'),    
    path('<int:pk>/', UserProfilAPIview.as_view())
]