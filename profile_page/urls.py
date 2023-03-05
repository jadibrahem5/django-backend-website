from django.urls import  path
from .views import  task_create,task_delete,task_update,home_page ,ExerciseCreateView, ExerciseDetailView ,ExerciseUpdateView ,ExerciseDeleteView, day_create, list, new_day, edit_day, delete_day, routin_delete
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
urlpatterns =[
    path('profile_page/', home_page,name= "profile"),
    path('task_create/', task_create, name='task_create'),
    path('task_delete/<int:id>/', task_delete, name='task_delete'),
    path('task_update/<int:id>/', task_update, name='task_update'),
    path( 'create/', ExerciseCreateView.as_view(),name="exercise_create"),
    path("detail/<int:pk>/",ExerciseDetailView.as_view(),name="exercise_detail"),
    path("update/<int:pk>",ExerciseUpdateView.as_view(),name="exercise_update"),
    path("delete/<int:pk>",ExerciseDeleteView.as_view(),name="exercise_confirm_delete"),
    path('day_create/', day_create, name='day_create'),
    path('new_day/', new_day, name='new_day'),
    path('list/<int:id>/',list ,name= "list"),
    path('edit_day/<int:id>/', edit_day,name= "edit_day"),
    path('delete_day/<int:id>/', delete_day,name= "delete_day"),
    path('routin_delete/<int:id>/', routin_delete,name= "routin_delete"),
]