from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Job
# from .forms import JobModelForm

class Jobs(generic.ListView):
    model = Job
    context_object_name = 'jobs'
    queryset = Job.objects.all()
    template_name = 'jobs/job_list.html'

class JobDetail(generic.DetailView):
    model = Job
    context_object_name = 'job'
    def get_object(self):
        id = self.kwargs.get("pk")
        return  get_object_or_404(Job,id=id)

# class JobCreate(generic.edit.CreateView):
#         model = Job
#         fields = "__all__"