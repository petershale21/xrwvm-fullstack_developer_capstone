# from django.contrib import admin
# from .models import related models


from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1  # Number of empty forms to display
    fields = ('name', 'type', 'year', 'engine', 'color')  # Control displayed fields
    ordering = ('-year',)  # Newest models first

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'year', 'type', 'created_date')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name')
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description', 'founded_year')
    search_fields = ('name', 'description', 'headquarters')
    list_filter = ('founded_year',)

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)