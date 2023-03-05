from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import  reverse
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    def __str__(self):
        return self.title
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    todo_list = models.ForeignKey(ToDoList,default=None,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse(
            "task_update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due}"

    class Meta:
        ordering = ["due"]

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

    def __str__(self):
        return self.name



class Routin(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_start=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Day_exercise(models.Model):
    # day1 = 'day1'
    # day2 = 'day2'
    # day3= 'day3'
    # day4 = 'day4'
    # day5 = 'day5'
    # days_choice = [
    #     (day1, 'day1'),
    #     (day2, 'day2'),
    #     (day3, 'day3'),
    #     (day4, 'day4'),
    #     (day5, 'day5'),
    # ]
    # days = models.CharField(
    #     max_length=10,
    #     choices= days_choice,
    #     default=day1,
    # )
    name = models.CharField(max_length=100)
    routin = models.ForeignKey(Routin, default=None, null=True, on_delete=models.CASCADE)
    exercise = models.ManyToManyField(Exercise, null=True, blank=True)

    def __str__(self):
        return self.name






