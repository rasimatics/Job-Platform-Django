from django.forms.models import ModelForm
from jobs.models import Job


class CreateAndUpdateJobForm(ModelForm):
    class Meta:
        model = Job
        exclude = ('slug',)