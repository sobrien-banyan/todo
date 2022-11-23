from django.shortcuts import render

from django.views import View
from todo_app.models import Task
from todo_app.forms import TaskForm

# Create your views here.

class HomeView(View):
    def get(self, request):
        task_form = TaskForm()
        tasks = Task.objects.all()

        html_data = {
            'task_list': tasks,
            'form': task_form,
        }

        return render(
            request=request,
            template_name='index.html',
            context=html_data,
        )

    def post(self, request):
        print(request.POST)
        task_form = TaskForm(request.POST)

        task_form.save()
        tasks = Task.objects.all()
        print(tasks)
        # task_form = TaskForm()
        html_data = {
            'task_list': tasks,
            'form': task_form,
        }

        return render(
            request=request,
            template_name='index.html',
            content_type=html_data,
        )