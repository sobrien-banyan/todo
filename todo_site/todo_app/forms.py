from django import forms

from todo_app.models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {'description': forms.TextInput(attrs={'size': 80})}
        fields = ['description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __def__(self, *args, **kwargs):
        task = kwargs.pop('task_object')
        super().__init__(*args, **kwargs)

        # self.instance is the comment we are creating with this form
        self.instance.task = task