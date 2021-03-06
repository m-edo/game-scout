# Generated by Django 4.0 on 2022-02-02 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0028_alter_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='sale',
            field=models.IntegerField(blank=True, default=0, help_text='Enter the sale value', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
