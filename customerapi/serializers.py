from rest_framework import serializers
from django.contrib.auth.models import User, Group
from . import models
class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Customers
        #fields = '__all__' #This should work :)
        fields = ["url","ledger_id","ledger_title","login_id","login_password","contact_number","email","address","fcm_token"]
        
class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Products
        #fields = '__all__' #This should work :)
        fields = [
            "url",
            "item_id",
            "item_title",
            "item_description",
            "months",
            "size",
            "origin",
            "weight",
            "price",
            "item_image"
            ]
            
class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Orders
        fields = "__all__"
class OrderTimeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderTimeLine
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']