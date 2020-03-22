from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    description = models.TextField()
    email = models.EmailField()
    number = models.CharField(max_length=15)
    finished_date = models.DateField()

    def __str__(self):
        return self.job_name