from django.contrib import admin

from .models import Menu_Regular_Pizza, Menu_Sicilian_Pizza, Menu_Topping, Menu_Sub, Menu_Pasta, Menu_Salad, Menu_Dinner_Platter, Menu_Sub_Extra, Order, All_Order

# Register your models here.
admin.site.register(Menu_Regular_Pizza)
admin.site.register(Menu_Sicilian_Pizza)
admin.site.register(Menu_Topping)
admin.site.register(Menu_Sub)
admin.site.register(Menu_Pasta)
admin.site.register(Menu_Salad)
admin.site.register(Menu_Dinner_Platter)
admin.site.register(Menu_Sub_Extra)
admin.site.register(Order)
admin.site.register(All_Order)
