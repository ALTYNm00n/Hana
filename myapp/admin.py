from django.contrib import admin
from django.conf import settings
from myapp.models import (
    Home_restaurant, 
    MenuItem, 
    ComingSoon, 
    RestaurantInfo, 
    ContactInfo, 
    ClientReview,
)



class Home_restaurantAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= settings.MAX_COMPANY_COUNT:
            return False
        return super().has_add_permission(request)

admin.site.register(Home_restaurant, Home_restaurantAdmin)
admin.site.register(MenuItem)
admin.site.register(ComingSoon)
admin.site.register(RestaurantInfo)
admin.site.register(ContactInfo)
admin.site.register(ClientReview)