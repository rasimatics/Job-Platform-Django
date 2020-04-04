from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

class Category(models.Model):
    category = models.TextField(max_length=40)

    def __str__(self):
        return  self.category


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    post_title = models.TextField(max_length=100)
    post_body = models.TextField()
    price = models.IntegerField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField()

    def save(self,*args,**kwargs):
        extension = 1
        self.slug = slugify(self.post_title)
        slug = self.slug
        while(Post.objects.filter(slug=slug).exists()):
            slug = self.slug
            slug = "{slug}{random}".format(slug=slug,random=extension)
            extension+=1

        self.slug=slug
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return  self.post_title

    class Meta:
        ordering = ['-pk']
