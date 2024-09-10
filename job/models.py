from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance, filename):
    imagename, extention= filename.split('.')
    return f"jobs/{instance.id}.{extention}"

class Job(models.Model):
    title= models.CharField(max_length=100)
    job_type= models.CharField(max_length=15, choices=JOB_TYPE)
    description= models.TextField(max_length=1000)
    published_at= models.DateField(auto_now=True)
    vacancy= models.IntegerField(default=1, validators=[MinValueValidator(0)]) #number of available places
    salary= models.IntegerField(default=0, validators=[MinValueValidator(0)])
    experience= models.IntegerField(default=0, validators=[MinValueValidator(0)])
    category= models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)      # The '' for the Category because it comes later, if it was before we needn't the ''
    image= models.ImageField(upload_to=image_upload)
    slug= models.SlugField(blank=True, null=True)
    location = models.CharField(max_length=100)

    def save(self,*args,**kwargs):
        self.slug= slugify(self.title)
        super(Job, self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name= models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    webiste = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name