from django.urls import path

from todo_app.views import HomeView, TaskDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:task_id>', TaskDetailsView.as_view(), name='task_details'),
]