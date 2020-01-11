from rest_framework import serializers
from . import models

class OrderTimeLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OrderTimeLine
        fields = "__all__"