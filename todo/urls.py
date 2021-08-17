from django.urls import path

from todo import views

urlpatterns = [
    path('tasks/', views.views.TaskListView.as_view(), name='tasks-list'),
    path('tasks/<int:task_pk>', views.TaskDetailView.as_view(), name='tasks-datail'),
]