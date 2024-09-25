from django.db import models

class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ItemCategory'
        verbose_name_plural = 'itemCategories'
        
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ShopApp')
    prize = models.FloatField()
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        
    def __str__(self):
        return self.name