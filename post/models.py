from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    category = models.TextField(max_length=40)


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    post_title = models.TextField(max_length=100)
    post_body = models.TextField()
    price = models.IntegerField()


    
