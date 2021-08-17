from todo.models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',
                  'title',
                  'message',
                  'conclusion_at',
                  'concluded',
                  'create_at',
                  'create_by')
        read_only_fields = ('id', 'create_at', 'create_by')