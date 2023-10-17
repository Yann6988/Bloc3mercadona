from django.contrib import admin
from store.models import ProductMeat, ProductVegetable, ProductFish, ProductFruit, ProductCosmeticH, ProductCosmeticF

@admin.register(ProductMeat)
class ProductMeatAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "promo", "percent", "promo_date_end")
    list_editable = ("price", "promo", "percent", "promo_date_end")

@admin.register(ProductVegetable)
class ProductMeatAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "promo", "percent", "promo_date_end")
    list_editable = ("price", "promo", "percent", "promo_date_end")

@admin.register(ProductFish)
class ProductMeatAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "promo", "percent", "promo_date_end")
    list_editable = ("price", "promo", "percent", "promo_date_end")

@admin.register(ProductFruit)
class ProductMeatAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "promo", "percent", "promo_date_end")
    list_editable = ("price", "promo", "percent", "promo_date_end")

@admin.register(ProductCosmeticH)
class ProductMeatAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "promo", "percent", "promo_date_end")
    list_editable = ("price", "promo", "percent", "promo_date_end")

@admin.register(ProductCosmeticF)
class ProductMeatAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "promo", "percent", "promo_date_end")
    list_editable = ("price", "promo", "percent", "promo_date_end")