from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import CreateAndUpdateJobForm
from .models import Job

class Jobs(ListView):
    model = Job
    context_object_name = 'jobs'
    queryset = Job.objects.all()
    template_name = 'jobs/job_list.html'

class JobCreate(CreateView):
    template_name = 'jobs/job_create.html'
    model = Job
    form_class = CreateAndUpdateJobForm

    def form_valid(self, form):
        form=form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect('alljobs')


class JobDetail(DetailView):
    model = Job
    context_object_name = 'job'

    def get_object(self):
        slug = self.kwargs.get("slug")
        return  get_object_or_404(Job, slug=slug)


class JobUpdate(UpdateView):
    model = Job
    form_class = CreateAndUpdateJobForm


    def get_object(self):
        job = get_object_or_404(Job, slug=self.kwargs.get('slug'))
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
        job = get_object_or_404(Job, slug=self.kwargs.get('slug'))
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

class SearchResultsJobs(ListView):
    model = Job
    template_name = 'jobs/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Job.objects.filter(
            Q(job_name__contains=query) |
            Q(company_name__icontains=query) |
            Q(description__icontains=query)
        )
        return object_list