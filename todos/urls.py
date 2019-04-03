from django.urls import path
from . import views

urlpatterns = [
    path('signup/' , views.SignUp , name = 'signup'),
    path('create/' , views.ToDoCreate , name='create'),
    path('detail/' , views.ToDoDetail , name='detail'),
    path('update/<int:pk>/' , views.ToDoUpdate , name='update'),
    path('delete/<int:pk>/' , views.ToDoDelete , name='delete'),
]
