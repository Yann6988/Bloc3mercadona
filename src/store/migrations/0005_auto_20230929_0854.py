# Generated by Django 3.1.7 on 2023-09-29 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20230929_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmeat',
            name='promo_date_end',
            field=models.DateField(blank=True, null=True, verbose_name='Date fin de promotion'),
        ),
    ]
