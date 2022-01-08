# Generated by Django 4.0 on 2022-01-08 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ecommerce', '0019_alter_transaction_date_time_delete_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to='auth.user'),
        ),
    ]
