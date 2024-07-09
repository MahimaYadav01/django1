from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
# Create your views here.

def home(request):
    return HttpResponse("hello mahima,its okay you got this")
def index(request):
    # context={
    #     "variable":"life sucks"
    # }
    return render(request,"index.html")

def contact(request):
    if request.method=="POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email=request.POST.get("email")
        phnno=request.POST.get("phnno")
        desc=request.POST.get("desc")
        
        contact=Contact(fname=fname,lname=lname, email=email, phnno =phnno ,desc=desc ,date=datetime.today())
        contact.save()
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def services(request):
     return render(request,"services.html")
def blog(request):
    return HttpResponse("why")
