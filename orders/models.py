from django.db import models
from members.models import Member

class OrderStatus(models.TextChoices):      # 주문 상태를 구현 하고 싶었는데, 아직 완성 못함. response객체에 status가 안보여짐.
    PREPARING = 'PREPARING', 'Preparing'
    DONE = 'DONE', 'Done'

class Order(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=OrderStatus.choices, default=OrderStatus.PREPARING)

    class Meta:
      db_table = 'orders'