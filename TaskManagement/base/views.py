from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskManagement
from .forms import TaskRead
from django.contrib import messages
# Create your views here.

def home(request):
    task = TaskRead(request.POST or None)
    if task.is_valid():
        task.save()
        messages.success(request,'created successfully')
        return redirect('read')
    context = {'task':task}
    return render(request,'home.html',context)

def read(request):
    task = TaskManagement.objects.all().order_by('-id')
    context = {'task':task}
    return render(request,'read.html',context)

def update(request, pk):
    task = get_object_or_404(TaskManagement, id=pk)  # correct method
    if request.method == 'POST':
        form = TaskRead(request.POST, instance=task)  # bind with POST + instance
        if form.is_valid():
            form.save()
            messages.success(request,'updated successfully')
            return redirect('read')  # redirect after update
    else:
        form = TaskRead(instance=task)  #  pre-fill with old data
    context = {'task': form}
    return render(request, 'update.html', context)


def delete(request,pk):
    task = get_object_or_404(TaskManagement,id = pk)
    if request.method =="POST":
        task.delete()
        messages.success(request,'deleted successfully')
        return redirect('read')
    context = {'task': task}
    return render(request, 'delete.html',context)