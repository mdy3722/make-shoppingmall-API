from rest_framework import serializers
from .models import Member, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['city', 'street', 'zipcode']

class MemberSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    address = AddressSerializer()

    class Meta:
        model = Member
        fields = ['id', 'name', 'address']
    
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)

        member = Member.objects.create(address=address, **validated_data)
        return member
    
    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address

        # Update Address instance
        for attr, value in address_data.items():
            setattr(address, attr, value)
        address.save()

        # Update Member instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance
