from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def output_todo_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "todo/todo_list.html", context)


def create_todo_item_manual(request):
    if request.method == "GET":
        return render(request, "todo/add_item_manual.html")
    elif request.method == "POST":
        name = request.POST.get("item_name")
        done = request.POST.get("item_done") == 'on'
        Item.objects.create(name=name, done=done)
        return redirect("/")

def create_todo_item_auto(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            
    form = ItemForm()
    context = {
        'form_generated' : form
    }
    return render(request, "todo/add_item_auto.html", context)
