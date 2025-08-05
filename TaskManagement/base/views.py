from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskManagement
from .forms import TaskRead
from django.contrib import messages
from django.db.models import Q   #this is a one type of method to search
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
    search = request.GET.get('q')
    if search:
        task = TaskManagement.objects.filter(
            Q(name__icontains =  search) |
            Q(task_name__icontains =  search) |
            Q(contact__icontains =  search) |
            Q(description__icontains =  search) |
            Q(priority__icontains =  search) |
            Q(status__icontains =  search) |
            Q(due_date__icontains =  search) |
            Q(created_at__icontains =  search) |
            Q(updated_at__icontains =  search) 
        )
    else:
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