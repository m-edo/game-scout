# Generated by Django 4.0 on 2022-01-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0016_alter_transaction_payment_method_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-date_time'], 'verbose_name_plural': 'Transactions'},
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='time',
        ),
        migrations.AddField(
            model_name='key',
            name='sale_expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]