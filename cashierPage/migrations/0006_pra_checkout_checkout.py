# Generated by Django 4.2.2 on 2023-06-14 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cashierPage', '0005_alter_product_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='pra_checkOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashierPage.product')),
            ],
        ),
        migrations.CreateModel(
            name='checkOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ManyToManyField(blank=True, null=True, to='cashierPage.pra_checkout')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]