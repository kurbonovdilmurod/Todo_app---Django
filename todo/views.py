from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import TodoForm
from .models import Todo
from django.contrib import messages


def view_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    context = {
        'todo': todo
    }

    return render(request, 'todo/view_todo.html', context)



def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Added To List!'))
            return redirect('home')
        else:
            return redirect('add_todo')

    else:
        form = TodoForm()
        context = {
            'form': form,
        }

        return render(request, 'todo/add_todo.html', context)



def edit_todo(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=pk)

        form = TodoForm(request.POST or None, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')

    else:
        todo = Todo.objects.get(pk=pk)
        return render(request, 'todo/edit_todo.html', {'todo':todo})




def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        todo.delete()
        messages.warning(request, ('Item Has Been Deleted!'))
        return redirect('home')

    context = {
        'todo': todo,
    }
    return render(request, 'todo/delete_todo.html', context)


def cross_off_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()
    return redirect('home')

def uncross_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = False
    todo.save()
    return redirect('home')
