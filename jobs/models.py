from django.contrib.auth import get_user_model
from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=20, default="")
    company_name = models.CharField(max_length=20)
    description = models.TextField()
    email = models.EmailField()
    number = models.CharField(max_length=15)
    finished_date = models.DateField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,editable=False)

    def __str__(self):
        return self.job_name