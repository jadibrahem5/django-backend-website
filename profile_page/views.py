from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import Task ,Exercise , Routin ,Day_exercise ,ToDoList
from .forms import TaskForm , UpdateForm, RoutinForm, DaysForm ,EditForm
# Create your views here.
@login_required(login_url="login")
def home_page(request):
    todolist= ToDoList.objects.all()
    queryset = Task.objects.order_by('complete', 'due')
    exercises = Exercise.objects.all()
    routin= Routin.objects.all()
    day = Day_exercise.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        listname = ToDoList()
        listname.title = request.POST.get('listname')
        listname.save()
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('profile')
 #   if request.user != Task.user:
  #      return HttpResponse('Your not  allowed here!!')
    context={
        'object_list':queryset,
        'exercises': exercises,
         'routin': routin,
         'day': day,
        'form':form ,
        'todolist':todolist,
    }
    return render(request, 'profile_page/profile.html', context)
@login_required(login_url="login")
def list(request,id):
    obj = get_object_or_404(ToDoList, id=id)
    tasks = Task.objects.all()
    if request.method == "POST":
        obj.delete()
        return redirect('profile')
    context={
        'object':obj,
        'tasks':tasks
    }
    return  render(request, 'profile_page/list.html', context)


@login_required(login_url="login")
def task_detail(request, id):
    obj = get_object_or_404(Task, id=id)
    context={
        'object':obj
    }
    return  render(request, 'goals/goal_detail.html', context)
@login_required(login_url="login")
def task_create(request):
    form = TaskForm
    form.user = request.user
    if request.method =='POST':
        form = TaskForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('profile')
    context={'form':form}
    return  render(request, 'profile_page/task_create.html',context)

@login_required(login_url="login")
def task_delete(request, id):
    obj = get_object_or_404(Task, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('profile')
    context = {
        "object": obj
    }
    return  render(request, 'profile_page/task_delete.html',context)
@login_required(login_url="login")
def task_update(request, id):
    obj = get_object_or_404(Task, id=id)
    form = UpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('profile')
    context = {'form': form}
    return  render(request, 'profile_page/task_update.html',context)



class ExerciseCreateView(CreateView):
  model = Exercise
  fields = ["name", "sets", "reps", "weight"]
  success_url = reverse_lazy("profile")

  def form_valid(self, form):
    form.instance.created_by = self.request.user
    return super().form_valid(form)




class ExerciseListView(ListView):
  model = Exercise
  context_object_name = "exercises" # friendly queryset name for the template
  def form_valid(self, form):
    form.instance.created_by = self.request.user
    return super().form_valid(form)

class ExerciseDetailView(DetailView):
      model = Exercise
      context_object_name = "exercise"

      def form_valid(self, form):
          form.instance.created_by = self.request.user
          return super().form_valid(form)

class ExerciseUpdateView(UpdateView):
  model = Exercise
  fields = ["name", "sets", "reps", "weight"]
  success_url = reverse_lazy("profile")
  def form_valid(self, form):
    form.instance.created_by = self.request.user
    return super().form_valid(form)

class ExerciseDeleteView(DeleteView):
  model = Exercise
  success_url = reverse_lazy("profile")


def day_create(request):
    form = RoutinForm
    form.user = request.user
    if request.method =='POST':
        # routname=Routin()
        # routname.name = request.POST.get('routname')
        # routname.save()
        form = RoutinForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('profile')
    context={'form':form}
    return  render(request, 'profile_page/day_create.html',context)


def new_day(request):
    form = DaysForm
    if request.method =='POST':
        form = DaysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context={'form':form}
    return  render(request, 'profile_page/new_day.html',context)

def edit_day(request, id):
    obj = get_object_or_404(Day_exercise, id=id)
    form = EditForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('profile')
    context = {'form': form}
    return  render(request, 'profile_page/edit_day.html',context)

def delete_day(request, id):
    obj = get_object_or_404(Day_exercise, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('profile')
    context = {
        "object": obj
    }
    return render(request, 'profile_page/delete_day.html', context)
def routin_delete(request, id):
    obj = get_object_or_404(Routin, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('profile')
    context = {
        "object": obj
    }
    return render(request, 'profile_page/routin_delete.html', context)

