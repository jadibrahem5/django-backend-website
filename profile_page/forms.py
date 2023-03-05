from django import forms
from django.forms import  ModelForm
from .models import Task ,Routin, Day_exercise, Exercise
class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)
	description = forms.Textarea()
	due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)
	class Meta:
		model = Task
		fields = ['title', 'due','description','todo_list']
class UpdateForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))

	class Meta:
		model = Task
		fields = ['title', 'due', 'complete']
# class TaskForm(ModelForm):
#     class Meta:
#         model =Task
#
#         fields = [
#
#             'title',
#             'description',
#             'complete',
#
#         ]
# DEMO_CHOICES =(
#     ("day1", "day1"),
#     ("day2", "day2"),
#     ("day3", "day3"),
#     ("day4", "day4"),
#     ("day5", "day5"),
# )
class RoutinForm(forms.ModelForm):
	name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'routin name...'}), label="your routin name:")
	class Meta:
		model = Routin
		fields = ['name']

class DaysForm(forms.ModelForm):
   name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'inter the new day...'}), label="your day name:")
   class Meta:
	   model = Day_exercise
	   fields = ['name','exercise','routin']


class EditForm(ModelForm):
    class Meta:
        model =Day_exercise
        fields = '__all__'