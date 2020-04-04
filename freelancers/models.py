from django.db import models
from django.template.defaultfilters import slugify


class NewFreelancer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    skills = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    slug = models.SlugField(null=True)


    def save(self,*args,**kwargs):
        extension = 1
        self.slug = slugify(f'{self.name}{self.surname}')
        slug = self.slug
        while(NewFreelancer.objects.filter(slug=slug).exists()):
            slug = self.slug
            slug = "{slug}{random}".format(slug=slug,random=extension)
            extension+=1

        self.slug=slug
        super(NewFreelancer, self).save(*args, **kwargs)

    def __str__(self):
        return self.name+" "+self.surname

