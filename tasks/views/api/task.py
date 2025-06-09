from rest_framework.viewsets import ViewSet
from tasks.models import Task, TaskStatus
from tasks.serializers.task import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


class TaskAPI(ViewSet):

    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        try:
            queryset = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["patch"])
    def complete_task(self, request, pk):
        try:
            queryset = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        queryset.status = TaskStatus.DONE.value
        queryset.save()

        serializer = TaskSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        try:
            queryset = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        object_title = queryset.title
        queryset.delete()
        return Response({'title': object_title}, status=status.HTTP_200_OK)