from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from teacher.forms import *
from teacher.models import *


class HomePageView(TemplateView):
    template_name = 'teacher/teacher_home.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form_name = request.POST.get('form_name')
        if form_name == 'grade_form':
            grade_value = request.POST.get('value')
            task = (Task.objects.filter(id=request.POST['task_id']))[0]
            user = (CustomUser.objects.filter(id=request.POST['user_id']))[0]
            grades = Grade.objects.get_or_create(task=task, user=user)
            Grade.objects.filter(task=task, user=user).update(value=grade_value)
        elif form_name == 'delete_task_form':
            task_id = request.POST.get('task_id')
            Task.objects.filter(id=task_id).delete()
        return HttpResponseRedirect(request.path)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['users'] = CustomUser.objects.filter(is_student=True)
        context['tasks'] = Task.objects.all()
        context['grades'] = Grade.objects.all()
        return context


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'teacher/registration.html'
    success_url = reverse_lazy('login_page')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'teacher/login_page.html'
    next_page = reverse_lazy('home_page')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'teacher/create_task.html'
    success_url = reverse_lazy('home_page')


def logout_user(request):
    logout(request)
    return redirect('home_page')
