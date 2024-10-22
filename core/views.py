from django.shortcuts import render
from todo.models import Todo

def home(request):
    all_todos = Todo.objects.all()
    context = {
        'all_todos': all_todos,
    }
    return render(request, 'core/home.html', context)
