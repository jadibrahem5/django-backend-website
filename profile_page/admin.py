from django.contrib import admin
from .models import Task,Exercise,Routin,Day_exercise, ToDoList
# Register your models here.
admin.site.register(Task)
admin.site.register(Routin)
admin.site.register(Day_exercise)
admin.site.register(Exercise)
admin.site.register(ToDoList)