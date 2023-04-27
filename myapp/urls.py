from django.urls import path 
from rest_framework.routers import DefaultRouter as DR


from myapp.views import(
    MenuCategoryView,
    MenuItemView,
    ComingSoonView,
    RestaurantInfoView,
    ContactInfoView,
    ClientReviewView,
)

router = DR()

router.register('menu_category', MenuCategoryView, basename='menu_category')
router.register('menuitems', MenuItemView, basename='menuitems')
router.register('comsoon', ComingSoonView, basename='comsoon')
router.register('restaurants_infos',RestaurantInfoView, basename='restaurants_infos')
router.register('contactinfos', ContactInfoView, basename='contactinfos')
router.register('client_rewiwes', ClientReviewView, basename='client_rewiwes')

urlpatterns =[]

urlpatterns += router.urls

urlpatterns = [

]

urlpatterns += router.urls