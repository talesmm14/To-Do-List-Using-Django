from rest_framework import serializers
from models import Task

class TaskSerializer(serializers.ModelSerializers):
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