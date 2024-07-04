from rest_framework import serializers
from items.models import Item, Order_item

class ItemSerializer(serializers.ModelSerializer):
    itemName = serializers.CharField(source='item_name')
    itemPrice = serializers.IntegerField(source='item_price')
    stockQuantity = serializers.IntegerField(source='stock_quantity')

    class Meta:
        model = Item
        fields = ['id', 'itemName', 'itemPrice', 'stockQuantity']

class ShoppinCartSerializer(serializers.Serializer):
    itemId = serializers.IntegerField(source='item.id')
    itemName = serializers.CharField(source='item.item_name')
    itemPrice = serializers.IntegerField(source='item.item_price', read_only=True)
    count = serializers.IntegerField()
    status = serializers.CharField(source='order_status', read_only=True)

    class Meta:
        model = Order_item
        fields = ['itemId', 'itemName', 'itemPrice', 'count', 'status']