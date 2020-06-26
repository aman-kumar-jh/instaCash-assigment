from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView , CreateView
from django.urls import reverse_lazy
from datetime import date

from .models import Task
from .forms import TaskForm

@login_required(login_url='login')
def TaskView(request):
    task_obj = Task.objects.filter(author=request.user)
    return render(request,'task_list.html',{'object_list':task_obj})

@login_required(login_url='login')
def TodayTaskList(request):
    startdate = date.today()
    task_obj = Task.objects.filter(date__range=[startdate,startdate])
    return render(request,'task_list.html',{'object_list': task_obj})

@login_required(login_url='login')    
def CompleteTask(request,pk):
    print(pk)
    task = get_object_or_404(Task,pk=pk)
    task.complete_task()
    return redirect('task_detail',pk=pk)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_new.html'
    form_class = TaskForm
    login_url = 'login'
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    login_url = 'login'
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')
    login_url = 'login'

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_edit.html'
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)    