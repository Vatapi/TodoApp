from django import forms
from .models import ToDoList
class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100 , label="Username" , required = True)
    email = forms.CharField(max_length=100 , label="Email", required = True)
    password = forms.CharField(max_length=100 , min_length=8 , required=True , widget=forms.PasswordInput())

class BookForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title' , 'content' , 'todo_date']
