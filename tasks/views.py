from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                title = form.cleaned_data['title'],
                text = form.cleaned_data['text'],
                author = request.user,
            )

            return redirect('list-tasks')
    else:
        form = TaskForm()

    return render(request, 'tasks/create.html',  {'form': form})

def read_task(request, task_id):
    task = get_object_or_404(Task, pk = task_id)
    return render(request, 'tasks/read.html',  {'task': task})



def list_tasks(request):
    tasks = Task.objects.filter(author=request.user)
    return render(request, 'tasks/list.html', {'tasks': tasks})



def delete_task(request, task_id):
    task = get_object_or_404(Task, pk = task_id)

    if task.author != request.user:
        return HttpResponseForbidden('вы не можете удалить этот пост')

    if request.method == 'POST':
        task.delete()
        return redirect('list-tasks')

    return render(request, 'tasks/delete.html', {'task': task})


def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if task.author != request.user:
        return HttpResponseForbidden('Вы не можете редактировать этот пост')


    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title_form = form.cleaned_data.get('title')
            text_form = form.cleaned_data.get('text')

            task.title = title_form

            task.text = text_form

            task.save()
            return redirect('list-tasks')
    else:
        form = TaskForm(initial={'title': task.title, 'text': task.text})     # при переходе будет форма с уже существующими данными 
        
    return render(request, 'tasks/update.html', {'form': form})


def home_page(request):
    return render(request, 'tasks/home.html')


def about_website(request):
    return render(request, 'tasks/about.html')