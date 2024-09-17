from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    image = models.ImageField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    # Defines model options that determines how Django handles the model at the database and admin level.
    class Meta:
        verbose_name = ('service') # Model´name that should be displayed in the admin level
        verbose_name_plural = ('services') # Model name that should be displayed in the admin level
    
    def __str__(self):
        return self.title