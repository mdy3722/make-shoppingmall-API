from django.db import models
from orders.models import Order
# from rest_framework.exceptions import ValidationError

class Item(models.Model):
    item_name = models.CharField(max_length=512)
    stock_quantity = models.IntegerField()
    item_price = models.IntegerField()
    order = models.ManyToManyField(Order, through='Order_item')

    class Meta:
      db_table = 'item'
    # def sub_stock(self, quantity, save=True):
    #     if self.stock_quantity - quantity < 0:
    #         raise ValidationError('재고 부족으로 주문이 불가능합니다.')
    #     self.stock_quantity -= quantity
    #     if save:
    #         self.save()
class Order_item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
      db_table = 'order_item'