# Generated by Django 4.2.2 on 2023-06-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashierPage', '0004_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
