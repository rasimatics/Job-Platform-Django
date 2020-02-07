from django.shortcuts import render

# Create your views here.

def freelancers(request):
    return render(request,"freelancers.html")
