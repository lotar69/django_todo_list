from django.urls import path

from .views import index, add_collection, add_task, get_tasks, delete_task, delete_collection


urlpatterns = [
    path('', index, name="home"),
    path('add-collection/', add_collection, name="add-collection"),
    path('add-task/', add_task, name="add-task"),
    path('delete-task/<int:task_pk>/', delete_task, name="delete-task"),
    path('delete-collection/<int:collection_pk>/', delete_collection, name="delete-collection"),
    path('get-tasks/<int:collection_pk>/', get_tasks, name="get-tasks"),
]