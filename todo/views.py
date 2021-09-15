from django.shortcuts import get_object_or_404, render, redirect
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


def update_todo_item_auto(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        item_new = ItemForm(request.POST, instance=item)
        if item_new.is_valid():
            item_new.save()
            return redirect("/")

    form = ItemForm(instance=item)
    context = {
        'form_generated' : form
    }
    return render(request, "todo/edit_item_auto.html", context)


def toggle_todo_done(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect("/")
