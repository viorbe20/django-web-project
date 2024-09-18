from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    
    # Defines model options that determines how Django handles the model at the database and admin level.
    class Meta:
        verbose_name = ('category') # Model´name that should be displayed in the admin level
        verbose_name_plural = ('categories') # Model name that should be displayed in the admin level
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    image = models.ImageField(upload_to='BlogApp', null=True, blank=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE) # Delete old posts if user is not logged in
    categories = models.ManyToManyField(Category) # One post can have multiple categories, and one category can have multiple posts
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    # Defines model options that determines how Django handles the model at the database and admin level.
    class Meta:
        verbose_name = ('post') # Model´name that should be displayed in the admin level
        verbose_name_plural = ('posts') # Model name that should be displayed in the admin level
    
    def __str__(self):
        return self.title