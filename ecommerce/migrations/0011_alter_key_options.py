# Generated by Django 3.2.7 on 2021-10-19 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_auto_20211015_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='key',
            options={'ordering': ['product', 'serial_key'], 'permissions': (('can_add_key', 'Add a new product key'),), 'verbose_name_plural': 'Keys'},
        ),
    ]
