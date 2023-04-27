from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend


from myapp.models import (
    MenuCategory, 
    MenuItem, 
    ComingSoon, 
    RestaurantInfo, 
    ContactInfo,
    ClientReview,
)

from myapp.serializers import (
    MenuCategorySerializer,
    MenuItemSerializer,
    ComingSoonSerializer,
    RestaurantInfoSerializer,
    ContactInfoSerializer,
    ClientReviewSerializer,
)

class MenuCategoryView(ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    def list(self, request, *args, **kwargs):
        return Response(MenuCategorySerializer(MenuCategory.objects.first()).data)

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