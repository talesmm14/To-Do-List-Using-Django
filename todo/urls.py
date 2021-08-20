from todo.views import index, TaskDetailView, TaskListView, update, concluded, delete
from django.urls import path

urlpatterns = [
    # Rest API
    path('api/tasks/', TaskListView.as_view(), name='tasks-list'),
    path('api/tasks/<int:task_pk>', TaskDetailView.as_view(), name='tasks-datail'),

    # Html forms
    path('', index, name='list'),
    path('concluded_task/<int:pk>/', concluded, name='concluded'),
    path('update_task/<int:pk>/', update, name='update'),
    path('delete_task/<int:pk>/', delete, name='delete'),
]
