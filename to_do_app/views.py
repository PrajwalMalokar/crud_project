from django.shortcuts import render,redirect, get_object_or_404
from .models import Task


# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request,pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        Task.objects.create(title=title, description=description, due_date=due_date)
        return redirect('task_list')
    return render(request, 'task_form.html')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('task_detail', pk=task.pk)
    return render(request, 'task_form.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_detail', pk=task.pk)

def task_incomplete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = False
    task.save()
    return redirect('task_detail', pk=task.pk)  