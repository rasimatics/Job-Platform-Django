from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Job

class Jobs(ListView):
    model = Job
    context_object_name = 'jobs'
    queryset = Job.objects.all()
    template_name = 'jobs/job_list.html'

class JobCreate(CreateView):
    template_name = 'jobs/job_create.html'
    model = Job
    fields = "__all__"

    def form_valid(self, form):
        form=form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect('alljobs')


class JobDetail(DetailView):
    model = Job
    context_object_name = 'job'

    def get_object(self):
        id = self.kwargs.get("pk")
        return  get_object_or_404(Job,id=id)


class JobUpdate(UpdateView):
    model = Job
    fields = "__all__"


    def get_object(self):
        job = get_object_or_404(Job, id=self.kwargs.get('pk'))
        if(job.user == self.request.user):
            return job
        else:
            return None

    def form_valid(self, form):
        form.save()
        return redirect('myjobs')


class JobDelete(DeleteView):
    model = Job
    success_url = reverse_lazy('alljobs')

    def get_object(self):
        job = get_object_or_404(Job, id=self.kwargs.get('pk'))
        if (job.user == self.request.user):
            return job
        else:
            return None

class MyJobs(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs/my_jobs.html'

    def get_queryset(self):
        queryset = Job.objects.filter(user=self.request.user)
        return queryset