from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import permissions

from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend


from myapp.models import (
    Home_restaurant, 
    MenuItem, 
    ComingSoon, 
    RestaurantInfo, 
    ContactInfo,
    ClientReview,
)

from myapp.serializers import (
    Home_restaurantSerializer,
    MenuItemSerializer,
    ComingSoonSerializer,
    RestaurantInfoSerializer,
    ContactInfoSerializer,
    ClientReviewSerializer,
)

class Home_restaurantView(ModelViewSet):
    queryset =  Home_restaurant.objects.all()
    serializer_class = Home_restaurantSerializer
    def list(self, request, *args, **kwargs):
        return Response(Home_restaurantSerializer(Home_restaurant.objects.first()).data)

class MenuItemView(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends=(
        DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,
    )
    filterset_fields=(
        'name',
    )
    search_fields=(
        'name',
    )
    ordering_fields=(
        'price','name',
    )
    
class ComingSoonView(ModelViewSet):
    queryset = ComingSoon.objects.all()
    serializer_class = ComingSoonSerializer
    
class RestaurantInfoView(ModelViewSet):
    queryset = RestaurantInfo.objects.all()
    serializer_class = RestaurantInfoSerializer
    
class ContactInfoView(ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    
class ClientReviewView(ModelViewSet):
    queryset = ClientReview.objects.all()
    serializer_class = ClientReviewSerializer