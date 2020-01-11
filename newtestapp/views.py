from newtestapp.models import OrderTimeLine
from newtestapp.serializers import OrderTimeLineSerializer
from rest_framework import viewsets

class PurchaseListViewSet(viewsets.ModelViewSet):
    queryset = OrderTimeLine.objects.all()
    serializer_class = OrderTimeLineSerializer
    filter_fields = ('order_id',)
class FeedViewSet(viewsets.ModelViewSet):
    model = OrderTimeLine
    serializer_class = OrderTimeLineSerializer

    def get_queryset(self):
        
        orderid = self.request.query_params.get('orderid', None)
        queryset = OrderTimeLine.objects.filter(order_id=orderid)
        return queryset
         