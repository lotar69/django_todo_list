from django.urls import path

from .views import index, add_collection, add_task, get_tasks

urlpatterns = [
    path('', index, name="home"),
    path('add-collection/', add_collection, name="add-collection"),
    path('add-task/', add_task, name="add-task"),
    path('get-tasks/<int:collection_pk>/', get_tasks, name="get-tasks"),
]