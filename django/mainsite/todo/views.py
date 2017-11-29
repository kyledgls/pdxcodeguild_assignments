from django.http import HttpResponse
from .models import TodoItem
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):


    todo_items = TodoItem.objects.all()
    context = {'todo_items': todo_items}

    return render(request, 'todo/index.html', context)


def savetodo(request):

    todo_text = request.POST['todo_text']

    todo_item = TodoItem(todo_text=todo_text)
    todo_item.save()

    # print(request.POST['todo_text'])

    return HttpResponseRedirect(reverse('todo:index'))
