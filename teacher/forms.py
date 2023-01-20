from django import forms
from django.forms import TextInput, PasswordInput, Textarea

from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
                               label='Логин')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
                                label='Пароль')
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторение пароля'}),
        label='Повторение пароля')

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
                               label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
                               label='Пароль')


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class GradeAddForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['value']
