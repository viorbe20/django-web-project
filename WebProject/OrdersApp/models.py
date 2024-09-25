from django.db import models
from django.contrib.auth import get_user_model
from ShopApp.models import Item
from django.db.models import Sum, F, FloatField

# Contains active user
User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.id
    
    @property
    def get_total(self):
        return self.orderItems_set.aggregate(
            total = Sum("price")*F("quantity"), output_field = FloatField()
        )["total"]
    
    class Meta:
        db_table = 'orders'
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ['id']
        
class OrderItems(models.Model):
    '''List that contains the details of each order item'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.quantity} unidades de {self.item_id.name}"
    
    class Meta:
        db_table = 'order_items'
        verbose_name = 'order item'
        verbose_name_plural = 'order items'
        ordering = ['id']
        
