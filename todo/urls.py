from todo.views import TaskListView, TaskDetailView
from django.urls import path

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks-list'),
    path('tasks/<int:task_pk>', TaskDetailView.as_view(), name='tasks-datail'),
]