from django.test import TestCase
from store.models import ProductMeat, ProductVegetable, ProductFish, ProductFruit, ProductCosmeticH, ProductCosmeticF

class ProductMeatTest(TestCase):
    def test_price_promo(self):
        productMeat = ProductMeat.objects.create(
            price=10,
            percent=50,
            promo=True,
        )

        self.assertEqual(productMeat.price_with_promotion, 5)

        productMeat.percent = 25
        productMeat.save()

        self.assertEqual(productMeat.price_with_promotion, 7.5)

        productMeat.promo = False
        productMeat.save()

        self.assertEqual(productMeat.price_with_promotion, 10)

class ProductVegetableTest(TestCase):
    def test_price_promo(self):
        productVegetable = ProductVegetable.objects.create(
            price=10,
            percent=50,
            promo=True,
        )

        self.assertEqual(productVegetable.price_with_promotion, 5)

        productVegetable.percent = 25
        productVegetable.save()

        self.assertEqual(productVegetable.price_with_promotion, 7.5)

        productVegetable.promo = False
        productVegetable.save()

        self.assertEqual(productVegetable.price_with_promotion, 10)

class ProductFishTest(TestCase):
    def test_price_promo(self):
        productFish = ProductFish.objects.create(
            price=10,
            percent=50,
            promo=True,
        )

        self.assertEqual(productFish.price_with_promotion, 5)

        productFish.percent = 25
        productFish.save()

        self.assertEqual(productFish.price_with_promotion, 7.5)

        productFish.promo = False
        productFish.save()

        self.assertEqual(productFish.price_with_promotion, 10)

class ProductFruitTest(TestCase):
    def test_price_promo(self):
        productFruit = ProductFruit.objects.create(
            price=10,
            percent=50,
            promo=True,
        )

        self.assertEqual(productFruit.price_with_promotion, 5)

        productFruit.percent = 25
        productFruit.save()

        self.assertEqual(productFruit.price_with_promotion, 7.5)

        productFruit.promo = False
        productFruit.save()

        self.assertEqual(productFruit.price_with_promotion, 10)

class ProductCosmeticHTest(TestCase):
    def test_price_promo(self):
        productCosmeticH = ProductCosmeticH.objects.create(
            price=10,
            percent=50,
            promo=True,
        )

        self.assertEqual(productCosmeticH.price_with_promotion, 5)

        productCosmeticH.percent = 25
        productCosmeticH.save()

        self.assertEqual(productCosmeticH.price_with_promotion, 7.5)

        productCosmeticH.promo = False
        productCosmeticH.save()

        self.assertEqual(productCosmeticH.price_with_promotion, 10)

class ProductCosmeticFTest(TestCase):
    def test_price_promo(self):
        productCosmeticF = ProductCosmeticF.objects.create(
            price=10,
            percent=50,
            promo=True,
        )

        self.assertEqual(productCosmeticF.price_with_promotion, 5)

        productCosmeticF.percent = 25
        productCosmeticF.save()

        self.assertEqual(productCosmeticF.price_with_promotion, 7.5)

        productCosmeticF.promo = False
        productCosmeticF.save()

        self.assertEqual(productCosmeticF.price_with_promotion, 10)
