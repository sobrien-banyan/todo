# sandwich-app

## steps taken to create this
1. Create virtual environment  ->      ‘python3 -m venv venv’
2. Activate it  ->   source venv/bin/activate
3. Install Django ‘pip install django’
4. Create a django project with ‘Django-admin startproject <project_name>’
5. ‘pip3 freeze > requirements.txt’
6. Run ‘python3 manage.py runserver’ to see if it worked. -> install Django in the app  ` ‘pip install django’`
7. Create an ‘app’ inside your project with ‘python3 manage.py startapp <app_name>’
8. Install your new app in your projects setting file


### In todo_site/setting add:
```
INSTALLED_APPS = [
    'todo_app.apps.TodoAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### In todo_site/urls.py add:
```
from django.urls import path

from todo_app.views import HomeView, TaskDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:task_id>', TaskDetailsView.as_view(), name='task_details'),
]
```

### In todo_app create a file called urls.py and add:
```
from django.urls import path

from todo_app.views import HomeView, TaskDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:task_id>', TaskDetailsView.as_view(), name='task_details'),
]
```


create model

```
from django.db import models

# Create your models here.

class Task(models.Model):
    description = models.CharField(max_length=255)
```

### run the following cammand 'python manage.py migrate'
### run the following command 'python3 manage.py makemigrations' then run 'python3 manage.py migrate'

## open python shell in terminal 'python3 manage.py shell'

usefull commands:
<Model>.objects.count()
<Model>.objects.get()
<Model>.objects.create() -> Task.objects.create(description= 'make dinner')
<Model>.objects.filter()
<Model>.objects.all()
<Model>.objects.<get/filter/all>.delete()
