# Generated by Django 3.1.7 on 2023-09-29 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20230929_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmeat',
            name='percent',
            field=models.IntegerField(default=0, verbose_name='Pourcentage promotion'),
        ),
        migrations.AlterField(
            model_name='productmeat',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Prix'),
        ),
    ]
