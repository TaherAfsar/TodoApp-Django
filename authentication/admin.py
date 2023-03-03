from atexit import register
from django.contrib import admin

from todo.models import Todo

# Register your models here.

admin.site.register(Todo)
