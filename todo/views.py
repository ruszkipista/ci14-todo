from django.shortcuts import render, redirect
from .models import Item

# Create your views here.


def output_todo_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "todo/todo_list.html", context)


def create_todo_item(request):
    if request.method == "GET":
        return render(request, "todo/add_item.html")
    elif request.method == "POST":
        name = request.POST.get("item_name")
        done = request.POST.get("item_done") == 'on'
        Item.objects.create(name=name, done=done)
        return redirect("/")