# Generated by Django 3.1.7 on 2023-09-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=38, unique=True, verbose_name='Produit')),
                ('slug', models.SlugField(blank=True, max_length=38, unique=True)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='products')),
                ('promo_date_end', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Produits',
            },
        ),
    ]
