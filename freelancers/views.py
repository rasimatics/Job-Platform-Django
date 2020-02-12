from django.shortcuts import render, redirect
from .models import NewFreelancer


def freelancers(request):
    return render(request, "freelancers.html")


def addFreelancer(request):
    if request.method == 'POST':
        print(request.user)
        freelancer = NewFreelancer(name=request.POST['name'], surname=request.POST['surname'],
                                   description=request.POST['description'], skills=request.POST['skills'],
                                   contact=request.POST['contact'])
        freelancer.save()
        return redirect('freelancers')
    else:
        # freelancers = NewFreelancer.objects.all()
        return render(request, "addFreelancer.html")
