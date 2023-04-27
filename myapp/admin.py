from django.contrib import admin
from django.conf import settings
from myapp.models import (
    MenuCategory, MenuItem, ComingSoon, RestaurantInfo, ContactInfo, ClientReview)


class MenuCategoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= settings.MAX_COMPANY_COUNT:
            return False
        return super().has_add_permission(request)

admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(MenuItem)
admin.site.register(ComingSoon)
admin.site.register(RestaurantInfo)
admin.site.register(ContactInfo)
admin.site.register(ClientReview)