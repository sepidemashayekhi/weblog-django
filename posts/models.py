from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class PublishManager(models.Model):
    def get_queryset(self):
        return super.get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices): # for status with use manager publish post when save them 
        DRAFT = 'DF' , 'Draft'
        PUBLISHED = 'PB' , 'Published'
    
    
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, 
                                on_delete=models.CASCADE ,# behavior to adopt when the referenced object , 
                                related_name='blog_posts') # many to one user-posts
    budy = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created =models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2 , choices=Status.choices ,default=Status.DRAFT) 
    
    objects = models.Manager() # the defult manager
    published = PublishManager() # my custom manager

    class Meta:
        ordering = ['-publish']  # for sort post in database
        indexes =[
            models.Index(fields=['-publish']) # ease creating database indexes
        ]

    
    def __str__(self) -> str:
        return self.title





