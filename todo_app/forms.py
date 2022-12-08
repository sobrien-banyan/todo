from django import forms

from todo_app.models import Task, Comment, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {'description': forms.TextInput(attrs={'size': 80})}
        fields = ['description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task_object')
        super().__init__(*args, **kwargs)

        # self.instance is the comment we are creating with this form
        self.instance.task = task

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

    def save(self, task):
        tag_name = self.data['name']

        try:
            tag = Tag.objects.get(name=tag_name)
        except Tag.DoesNotExist:
            tag = Tag.objects.create(name=tag_name)
        task.tags.add(tag)