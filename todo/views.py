from todo.serializers import TaskSerializer
from django.http import Http404
from rest_framework import views, status
from rest_framework.response import Response
from todo.models import Task
from todo.serializers import TaskSerializer

class TaskListView(views.APIView):
    def get(self, request, format=None):
        snippets = Task.objects.all()
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(views.APIView):
    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            return task
        except Task.DoesNotExist:
            raise  Http404

    def get(self, request, task_pk, format=None):
        snippets = self.get_object(task_pk)
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)

    def put(self, request, task_pk, format=None):
        snippets = self.get_object(task_pk)
        serializer = TaskSerializer(snippets, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_pk, format=None):
        snippets = self.get_object(task_pk)
        serializer = TaskSerializer(snippets, many=True)

        if serializer.is_valid():
            serializer.delete()
            return Response(status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)