from django.db import models


class ProductMeat(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=38, unique=True, verbose_name="Viande")
    price = models.FloatField(default=0.0, verbose_name='Prix')
    description = models.TextField(blank=True, verbose_name="Description")
    thumbnail = models.ImageField(upload_to="products", blank=False, null=True,verbose_name='Image produit')
    promo = models.BooleanField(default=False, verbose_name="Produit en promotion")
    percent = models.IntegerField(default=0, verbose_name='Pourcentage promotion')
    promo_start_date = models.DateField(blank=True, null=True, verbose_name='Date début de promotion')
    promo_date_end = models.DateField(blank=True, null=True, verbose_name='Date fin de promotion')

    class Meta:
        verbose_name = "Viande"

    def __str__(self):
        return self.title

    @property
    def price_with_promotion(self):
        if self.promo:
           return round(self.price - (self.price * self.percent / 100), 2)
        return self.price


class ProductVegetable(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=38, unique=True, verbose_name="Légume")
    price = models.FloatField(default=0.0, verbose_name='Prix')
    description = models.TextField(blank=True, verbose_name="Description")
    thumbnail = models.ImageField(upload_to="products", blank=False, null=True,verbose_name='Image produit')
    promo = models.BooleanField(default=False, verbose_name="Produit en promotion")
    percent = models.IntegerField(default=0, verbose_name='Pourcentage promotion')
    promo_start_date = models.DateField(blank=True, null=True, verbose_name='Date début de promotion')
    promo_date_end = models.DateField(blank=True, null=True, verbose_name='Date fin de promotion')

    class Meta:
        verbose_name = "Légume"

    def __str__(self):
        return self.title

    @property
    def price_with_promotion(self):
        if self.promo:
           return round(self.price - (self.price * self.percent / 100), 2)
        return self.price


class ProductFish(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=38, unique=True, verbose_name="Poisson")
    price = models.FloatField(default=0.0, verbose_name='Prix')
    description = models.TextField(blank=True, verbose_name="Description")
    thumbnail = models.ImageField(upload_to="products", blank=False, null=True,verbose_name='Image produit')
    promo = models.BooleanField(default=False, verbose_name="Produit en promotion")
    percent = models.IntegerField(default=0, verbose_name='Pourcentage promotion')
    promo_start_date = models.DateField(blank=True, null=True, verbose_name='Date début de promotion')
    promo_date_end = models.DateField(blank=True, null=True, verbose_name='Date fin de promotion')

    class Meta:
        verbose_name = "Poisson"

    def __str__(self):
        return self.title

    @property
    def price_with_promotion(self):
        if self.promo:
            return round(self.price - (self.price * self.percent / 100), 2)
        return self.price


class ProductFruit(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=38, unique=True, verbose_name="Fruit")
    price = models.FloatField(default=0.0, verbose_name='Prix')
    description = models.TextField(blank=True, verbose_name="Description")
    thumbnail = models.ImageField(upload_to="products", blank=False, null=True,verbose_name='Image produit')
    promo = models.BooleanField(default=False, verbose_name="Produit en promotion")
    percent = models.IntegerField(default=0, verbose_name='Pourcentage promotion')
    promo_start_date = models.DateField(blank=True, null=True, verbose_name='Date début de promotion')
    promo_date_end = models.DateField(blank=True, null=True, verbose_name='Date fin de promotion')

    class Meta:
        verbose_name = "Fruit"

    def __str__(self):
        return self.title

    @property
    def price_with_promotion(self):
        if self.promo:
            return round(self.price - (self.price * self.percent / 100), 2)
        return self.price

class ProductCosmeticH(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=38, unique=True, verbose_name="Cosmetique Homme")
    price = models.FloatField(default=0.0, verbose_name='Prix')
    description = models.TextField(blank=True, verbose_name="Description")
    thumbnail = models.ImageField(upload_to="products", blank=False, null=True,verbose_name='Image produit')
    promo = models.BooleanField(default=False, verbose_name="Produit en promotion")
    percent = models.IntegerField(default=0, verbose_name='Pourcentage promotion')
    promo_start_date = models.DateField(blank=True, null=True, verbose_name='Date début de promotion')
    promo_date_end = models.DateField(blank=True, null=True, verbose_name='Date fin de promotion')
    class Meta:
        verbose_name = "Cosmetique homme"

    def __str__(self):
        return self.title

    @property
    def price_with_promotion(self):
        if self.promo:
            return round(self.price - (self.price * self.percent / 100), 2)
        return self.price

class ProductCosmeticF(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=38, unique=True, verbose_name="Cosmetique Femme")
    price = models.FloatField(default=0.0, verbose_name='Prix')
    description = models.TextField(blank=True, verbose_name="Description")
    thumbnail = models.ImageField(upload_to="products", blank=False, null=True,verbose_name='Image produit')
    promo = models.BooleanField(default=False, verbose_name="Produit en promotion")
    percent = models.IntegerField(default=0, verbose_name='Pourcentage promotion')
    promo_start_date = models.DateField(blank=True, null=True, verbose_name='Date début de promotion')
    promo_date_end = models.DateField(blank=True, null=True, verbose_name='Date fin de promotion')

    class Meta:
        verbose_name = "Cosmetique femme"

    def __str__(self):
        return self.title

    @property
    def price_with_promotion(self):
        if self.promo:
            return round(self.price - (self.price * self.percent / 100), 2)
        return self.price