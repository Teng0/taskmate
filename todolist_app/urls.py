from django.urls import path,include
from todolist_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todolist', views.todolist, name="todolist"),
    path('delete/<task_id>', views.delete_task, name="delete_task"),
    path('complate/<task_id>', views.complate_task, name="complate_task"),
    path('Notcomplate/<task_id>', views.Notcomplate_task, name="Notcomplate_task"),
    path('edit/<task_id>', views.edit_task, name="edit_task"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact")
]
