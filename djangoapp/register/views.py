from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm



# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            print("registered")
            form.save()
            return HttpResponseRedirect ("/")
            
        else:
            print(form.errors)  # This will show why the form didn't validate
    else:
        form = RegisterForm()
    
    return render(response,"register/register.html", {"form":form})
