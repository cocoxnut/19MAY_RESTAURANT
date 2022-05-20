from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models

class TableViewSet(ModelViewSet):
    queryset = models.Table.objects.all()
    serializer_class = serializers.TableSerializer


class OrderViewSet(ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer


class MenuViewSet(ModelViewSet):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


# Create your views here.
