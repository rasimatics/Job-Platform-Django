from django.db import models
from django.contrib.auth.models import User


class NewFreelancer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    skills = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name+" "+self.surname

