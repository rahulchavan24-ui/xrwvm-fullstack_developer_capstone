from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline lets you add car models on the car make page
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


# CarModelAdmin
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    list_filter = ('car_make', 'type', 'year')


# CarMakeAdmin with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
