from rest_framework import viewsets
from .models import Products,Customers,Orders,OrderTimeLine
from . serializers import ProductsSerializer,UserSerializer, GroupSerializer, CustomersSerializer, OrdersSerializer, OrderTimeLineSerializer
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
class ProductsViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class CustomersViewset(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
class OrderViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
class OrderTimeLineViewset(viewsets.ModelViewSet):
    model = OrderTimeLine
    serializer_class = OrderTimeLineSerializer

    def get_queryset(self):
        
        orderid = self.request.query_params.get('orderid', None)
        queryset = OrderTimeLine.objects.filter(order_id=orderid)
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

