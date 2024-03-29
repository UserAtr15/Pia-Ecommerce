# Generated by Django 3.1.7 on 2021-11-04 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('address', models.CharField(max_length=255, verbose_name='Direccion del pedido')),
                ('time', models.DateTimeField(default='', verbose_name='Hora de Pedido')),
                ('order_product', models.ManyToManyField(to='products.Product')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
