# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0007_auto_20170320_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
            ],
        ),
        migrations.RemoveField(
            model_name='deliveryorder',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='deliveryorder',
            name='date_delivery',
        ),
        migrations.RemoveField(
            model_name='reservationorder',
            name='cart',
        ),
        migrations.AlterField(
            model_name='deliveryorder',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Имя заказчика'),
        ),
        migrations.AlterField(
            model_name='deliveryorder',
            name='tel_number',
            field=models.CharField(max_length=25, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images/coffee_types'),
        ),
        migrations.AlterField(
            model_name='reservationorder',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Имя заказчика'),
        ),
        migrations.AlterField(
            model_name='reservationorder',
            name='tel_number',
            field=models.CharField(max_length=25, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.DeliveryOrder'),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.Product'),
        ),
    ]
