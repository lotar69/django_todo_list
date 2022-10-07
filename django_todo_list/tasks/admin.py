from django.contrib import admin

# Register your models here.
from .models import Collection, Task

admin.site.register(Collection)
admin.site.register(Task)