from django.shortcuts import render, redirect
from .models import NewFreelancer
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def freelancers(request):
    if request.user.is_authenticated:
        try:
            profile_exist = NewFreelancer.objects.get(user=request.user)
        except NewFreelancer.DoesNotExist:
            profile_exist = False
    else:
        profile_exist = False
    all_freelancers = NewFreelancer.objects.all()
    return render(request, "freelancers/freelancers.html", {"freelancers": all_freelancers, "profile_exist": profile_exist})


@login_required(login_url='/login/')
def addFreelancer(request):
    if request.method == 'POST':
        freelancer = NewFreelancer(name=request.POST['name'], surname=request.POST['surname'],
                                   description=request.POST['description'], skills=request.POST['skills'],
                                   contact=request.POST['contact'], user=request.user)
        freelancer.save()
        return redirect('freelancers')
    else:
        return render(request, "freelancers/addFreelancer.html")


@login_required(login_url='/login/')
def editFreelancer(request):
    freelancer = NewFreelancer.objects.get(user=request.user)
    if request.method == 'POST':
        freelancer.name = request.POST['name']
        freelancer.surname = request.POST['surname']
        freelancer.description = request.POST['description']
        freelancer.skills = request.POST['skills']
        freelancer.contact = request.POST['contact']
        freelancer.save()
        return redirect('freelancers')
    else:
        return render(request, "freelancers/editFreelancer.html", {"freelancer": freelancer})


@login_required(login_url='/login/')
def deleteFreelancer(request):
    freelancer = NewFreelancer.objects.get(user=request.user)
    freelancer.delete()
    return redirect('freelancers')

@login_required(login_url='/login/')
def freelancerDetail(request,id):
    freelancer = NewFreelancer.objects.get(id=id)
    context = {"freelancer":freelancer}
    return render(request,"freelancers/freelancerDetail.html",context)

