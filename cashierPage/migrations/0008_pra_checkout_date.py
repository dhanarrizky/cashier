# Generated by Django 4.2.2 on 2023-06-17 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashierPage', '0007_pra_checkout_code_alter_checkout_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='pra_checkout',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]