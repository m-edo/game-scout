# Generated by Django 4.0 on 2022-01-08 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ecommerce', '0019_alter_transaction_date_time_delete_wishlist'),
        ('customer', '0011_remove_profile_sold_keys'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(blank=True, to='ecommerce.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Wishlists',
            },
        ),
    ]
