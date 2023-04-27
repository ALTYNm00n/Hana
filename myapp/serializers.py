from rest_framework import serializers
from myapp.models import (
    MenuCategory, 
    MenuItem, 
    ComingSoon, 
    RestaurantInfo, 
    ContactInfo, 
    ClientReview,
)



class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = (
            'id', 'image', 'price', 'name',
		)


class ComingSoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComingSoon
        fields = (
            'id', 'name', 'image', 'created_at', 
		)
        
class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantInfo
        fields = (
            'title', 'description', 'address', 'phone', 'email', 'hours', 'image',
        )	

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = (
            'id', 'name', 'email', 'message',
		)
        
class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = (
            'id', 'name', 'review', 'star_nbr',
		)
class MenuCategorySerializer(serializers.ModelSerializer):
    menuitems = MenuItemSerializer(many=True,read_only=True)
    comsoon = ComingSoonSerializer(many=True,read_only=True)
    restaurants_infos = RestaurantInfoSerializer(many=True,read_only=True)
    contactinfos = ContactInfoSerializer(many=True,read_only=True)
    client_rewiwes = ClientReviewSerializer(many=True,read_only=True)
    class Meta:
        model = MenuCategory
        fields = (
            'id', 'logo', 'name', 'description', 'phone_number', 'menuitems',\
            'comsoon',  'restaurants_infos', 'contactinfos', 'client_rewiwes',
        )
        
	