# Generated by Django 4.2.2 on 2023-06-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_product', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('price_buy', models.FloatField(blank=True, null=True)),
                ('price_sale', models.FloatField(blank=True, null=True)),
                ('discription', models.TextField(blank=True, null=True)),
                ('date_buy', models.DateField(auto_now_add=True, null=True)),
                ('sale_deadline', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
