# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryorder',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='deliverystaff',
            name='actual_order',
        ),
        migrations.RemoveField(
            model_name='reservationorder',
            name='cart',
        ),
        migrations.DeleteModel(
            name='DeliveryOrder',
        ),
        migrations.DeleteModel(
            name='DeliveryStaff',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ReservationOrder',
        ),
    ]
