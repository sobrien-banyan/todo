# sandwich-app

## steps taken to create this
1. Create virtual environment  ->      ‘python3 -m venv venv’
2. Activate it  ->   source venv/bin/activate
3. Install Django ‘pip install django’
4. Create a django project with ‘Django-admin startproject <project_name>’
5. ‘pip3 freeze > requirements.txt’
6. Run ‘python3 manage.py runserver’ to see if it worded. -> install Django in the app  ` ‘pip install django’`
7. Create an ‘app’ inside your project with ‘python3 manage.py startapp <app_name>’
8. Install your new app in your projects setting file


### In sandwich_server/setting add:
```
INSTALLED_APPS = [
    'sandwich_app.app.SandwichAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### In sandwich_server/urls.py add:
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sandwich/', include('sandwich_app.urls')),
]
```

### In sandwich_app create a file called urls.py and add:
```
from django.urls import path

urlpatterns = []
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
