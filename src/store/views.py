from django.shortcuts import render
from store.models import ProductMeat, ProductVegetable, ProductFish, ProductFruit, ProductCosmeticH, ProductCosmeticF

# Create your views here.


def index(request):
    productsMeat = ProductMeat.objects.all()
    productsVegetable = ProductVegetable.objects.all()
    productsFish = ProductFish.objects.all()
    productsFruit = ProductFruit.objects.all()
    productsCosmeticH = ProductCosmeticH.objects.all()
    productsCosmeticF = ProductCosmeticF.objects.all()


    return render(request, 'store/index.html', context={"productsMeat":productsMeat,
                                                                     "productsVegetable": productsVegetable,
                                                                     "productsFish": productsFish,
                                                                     "productsFruit": productsFruit,
                                                                     "productsCosmeticH": productsCosmeticH,
                                                                     "productsCosmeticF": productsCosmeticF})




