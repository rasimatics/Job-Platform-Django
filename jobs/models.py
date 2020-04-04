from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify


class Job(models.Model):
    job_name = models.CharField(max_length=20, default="")
    company_name = models.CharField(max_length=20)
    description = models.TextField()
    email = models.EmailField()
    number = models.CharField(max_length=15)
    finished_date = models.DateField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,editable=False)
    slug = models.SlugField()

    def save(self,*args,**kwargs):
        extension = 1
        self.slug = slugify(self.job_name)
        slug = self.slug
        while(Job.objects.filter(slug=slug).exists()):
            slug = self.slug
            slug = "{slug}{random}".format(slug=slug,random=extension)
            extension+=1

        self.slug=slug
        super(Job, self).save(*args, **kwargs)


    def __str__(self):
        return self.job_name