from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


# Create your views here.
def index(response, id):
    ls= ToDoList.objects.get(id=id)
    #the name save points to value save this is needed
    # {"save":["save"], "c1":["clicked"]} // this what happen sa html value and name sa button

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) =="clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) >2 :
                if not ls.item_set.filter(text=txt).exists():
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Duplicate item! Item already exists in the list.")
            else:
                print("invalid")

    return render(response,"main/list.html", {"ls":ls})



def home(response ):
    if response .user.is_authenticated:
        # If the user is logged in, render the main page.
        return render(response , "main/home.html")
    else:
        # If the user is not logged in, render the landing page.
        return render(response , "main/landing.html")




def create(response):
    
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(user=response.user, name=n)
            t.save()
            response.user.todolist.add(t)
            
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList() 
    return render(response, "main/create.html", {"form": form})  


def view(response):
    return render(response,"main/view.html", {})


#--------other example use of th---------
# def create(response):
#     if response.method == "POST":
#         th = CreateNewList(response.POST)
#         if th.is_valid():
#             n = th.cleaned_data["name"]
#             t = ToDoList(name=n)
#             t.save()
#         return HttpResponseRedirect("/%i" %t.id)  
#     else:
#         th = CreateNewList() 
#     return render(response, "main/create.html", {"th": th})  


