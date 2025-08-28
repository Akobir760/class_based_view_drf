from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserProfile, Task
from .serializers import UserSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.utils import timezone

class UserProfilAPIview(APIView):
    def get(self, request, pk = None):
        if pk:
            try:
                user = UserProfile.objects.get(pk=pk)
            except UserProfile.DoesNotExist:

                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = UserSerializer(user)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            users = UserProfile.objects.all()
            serializer = UserSerializer(users, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(
                data=serializer.errors
            )
        
    def put(self, request, pk):
        try:
            user = UserProfile.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(instance = user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

    def patch(self, request, pk):
        try:
            user = UserProfile.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(instance = user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class TaskAPIView(APIView):
    def get(self, request, pk = None):
        if pk:
            try:
                task = Task.objects.get(pk=pk)
            except Task.DoesNotExist:

                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = TaskSerializer(task)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            tasks = Task.objects.filter(status="todo", priority="high")
            serializer = TaskSerializer(tasks, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(data=serializer.errors)
        
    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        


class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)
    


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    


class TaskByStatusView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        status = self.kwargs.get("status")  
        return Task.objects.filter(user=self.request.user, status=status)
    


class OverdueTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        today = timezone.now().date()
        return Task.objects.filter(
            user=self.request.user,
            due_date__lt=today
        ).exclude(status='done')



