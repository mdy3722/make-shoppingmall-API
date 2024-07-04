from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    class Meta:
      db_table = 'address'

class Member(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    
    class Meta:
      db_table = 'member'