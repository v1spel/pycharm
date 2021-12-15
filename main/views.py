from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import CreateNewList, Delete
from .models import ToDoList, Item


# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "main/list.html", {"ls": ls})

    return render(response, "main/home.html", {})


def homedb(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

            return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})


def delete(response):
    if response.method == "POST":
        lol = Delete(response.POST)

        if lol.is_valid():
            ob = lol.cleaned_data["name"]
            dele = ToDoList.objects.get(name=ob)
            dele.delete()

        return HttpResponseRedirect("/")

    else:
        lol = Delete()

    return render(response, "main/delete.html", {"form": lol})


def home(response):
    return render(response, "shop/home.html", {})


def shop(response):
    return render(response, "shop/shop.html", {})


def order(response):
    ls = ToDoList.objects.get(id=18)

    if ls in response.user.todolist.all():

        if response.method == "POST":

            if response.POST.get("order"):
                tex = response.POST.get("new")

                if len(tex) > 9:
                    ls.item_set.create(text=tex, complete=False)
                else:
                    print("invalid")

                ls.save()
        return render(response, "shop/order.html", {})
    return render(response, "shop/home.html", {})


def views(response):
    return render(response, "main/views.html", {})
