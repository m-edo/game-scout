# Generated by Django 3.2.7 on 2021-10-05 17:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a product category (e.g. OS, game)', max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a product developer', max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Developers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a product genre', max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Genres',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a product publisher', max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Publishers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter product name', max_length=64)),
                ('publishing_date', models.DateField(help_text='Enter the product publishing date')),
                ('description', models.TextField(blank=True, help_text='Enter a description for the product', null=True)),
                ('pic', models.ImageField(blank=True, help_text='Select a picture for the product', null=True, upload_to='')),
                ('category', models.ForeignKey(help_text='Enter a product category', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.category')),
                ('developer', models.ForeignKey(help_text='Enter the product developer', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.developer')),
                ('genre', models.ForeignKey(help_text='Enter a product genre', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.genre')),
                ('publisher', models.ForeignKey(help_text='Enter the product publisher', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.publisher')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['name', 'developer'],
            },
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_key', models.CharField(help_text='Enter the serial key', max_length=64, unique=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Enter the price for the key', max_digits=10)),
                ('sale', models.PositiveIntegerField(blank=True, default=0, help_text='Enter the sale value', validators=[django.core.validators.MaxValueValidator(100)])),
                ('sold', models.BooleanField(default=False)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.product')),
            ],
            options={
                'verbose_name_plural': 'Keys',
                'ordering': ['product', 'serial_key'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('payment_method', models.CharField(blank=True, choices=[('Visa', 'Visa'), ('MasterCard', 'MasterCard'), ('Maestro', 'MasterCard'), ('PayPal', 'PayPal'), ('PaySafeCard', 'PaySafeCard')], help_text='Choose the payment method', max_length=16, null=True)),
                ('state', models.CharField(choices=[('Success', 'Success'), ('Pending', 'Pending'), ('Failure', 'Failure')], default='Pending', max_length=16)),
                ('key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.key')),
            ],
            options={
                'verbose_name_plural': 'Transactions',
                'ordering': ['date', 'time'],
                'unique_together': {('id', 'key')},
            },
        ),
    ]
