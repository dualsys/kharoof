from rest_framework import viewsets
from . import models
from . serializers import ProductsSerializer,UserSerializer, GroupSerializer, CustomersSerializer, OrdersSerializer, OrderTimeLineSerializer
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
class ProductsViewset(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = ProductsSerializer

class CustomersViewset(viewsets.ModelViewSet):
    queryset = models.Customers.objects.all()
    serializer_class = CustomersSerializer
class OrderViewset(viewsets.ModelViewSet):
    queryset = models.Orders.objects.all()
    serializer_class = OrdersSerializer
# class OrderTimeLineViewset(viewsets.ModelViewSet):
#     queryset = models.OrderTimeLine.objects.all()
#     serializer_class = OrderTimeLineSerializer

class OrderTimeLineView(generics.ListAPIView):
    queryset = models.OrderTimeLine.objects.all()
    serializer_class = OrderTimeLineSerializer

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


class LoginToApp(viewsets.ModelViewSet):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = models.Customers.objects.all()
    serializer_class = CustomersSerializer
    @action(detail=True, methods=['get'])
    def loginnow(self, request, user_name=None, password=None):
        return Response("test")
        # user = self.get_object()
        # serializer = CustomersSerializer(data=request.DATA)
        # if serializer.is_valid():
        #     user.set_password(serializer.data['password'])
        #     user.save()
        #     return Response({'status': 'password set'})
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)
      
# Create your views here.
