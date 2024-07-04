from rest_framework import serializers
from items.serializers import ShoppinCartSerializer
from items.models import Order_item, Item
from .models import Order
from .models import Member

class OrderItemSerializer(serializers.Serializer):
    itemId = serializers.IntegerField()
    itemName = serializers.CharField()
    count = serializers.IntegerField()

class OrderRequestSerializer(serializers.Serializer):
    member_id = serializers.IntegerField()
    items = OrderItemSerializer(many=True)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        member_id = validated_data.pop('member_id')
        member = Member.objects.get(id=member_id)
        order = Order.objects.create(member=member, **validated_data)

        for item_data in items_data:
            item = Item.objects.get(id=item_data['itemId'])
            Order_item.objects.create(order=order, item=item, count=item_data['count'])

        return order
    
class OrderResponseSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='id')
    member_id = serializers.IntegerField(source='member.id')
    items = ShoppinCartSerializer(many=True, source='order_item_set')
    order_date = serializers.DateTimeField()

    class Meta:
        model = Order_item
        fields = ['order_id', 'member_id', 'items', 'order_date']