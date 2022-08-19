from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ListForm
from django.contrib import messages

import requests

# Create your views here.


def create_view(request):
    form = ListForm(request.POST or None)
    context = {}
    context["form"] = form
    if form.is_valid():
        form.save()
        all_items = Item.objects.all
    return render(request, "index.html", context)


def view_list(request):
    context = {}
    context["dataset"] = Item.objects.all()

    return render(request, "viewlist.html", context)


def delete_item(request, list_id):
    item = Item.objects.get(pk=list_id)
    item.delete()
    return redirect("/todolist/viewlist")


def edit_item(request, list_id):
    context = {}
    item = Item.objects.get(pk=list_id)
    context["dataset"] = Item.objects.get(pk=list_id)
    if item.status == "COMPLETE":
        item.staus = "INCOMPLETE"
    elif item.status == "INCOMPLETE":
        item.status = "COMPLETE"
    item.save()
    return render(request, "editlist.html", context)


def edited(request, list_id):
    context = {}
    item = get_object_or_404(Item, pk=list_id)
    form = ListForm(request.POST or None, instance=Item)
    name = request.GET.get("id")
    print("form : ", form)
    print("name : ", name)
    print("req : ", request.POST)
    item.save()
    print(context)
    context["dataset"] = Item.objects.all()
    return render(request, "viewlist.html", context)
