from todo.models import Task
from django import forms


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Task
        fields = ('title',
                  'conclusion_at',
                  'concluded')

