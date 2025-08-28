from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserProfile, Task
from .serializers import UserSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status

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
                user = Task.objects.get(pk=pk)
            except Task.DoesNotExist:

                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = TaskSerializer(user)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            users = Task.objects.all()
            serializer = TaskSerializer(users, many=True)

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
