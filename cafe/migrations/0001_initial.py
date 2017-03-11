# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 17:25
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='ФИО заказчика')),
                ('tel_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=128, verbose_name='Адрес')),
                ('date_delivery', models.DateTimeField(verbose_name='Дата доставки')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeliveryStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='ФИО')),
                ('chat_id', models.CharField(max_length=32, verbose_name='ID Telegram')),
                ('actual_order',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cafe.DeliveryOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Стоимость')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='ФИО заказчика')),
                ('tel_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('date_visit', models.DateTimeField()),
                ('count_visitors', models.PositiveSmallIntegerField(verbose_name='Количество посетителей')),
                ('number_place', models.PositiveSmallIntegerField(verbose_name='Номер стола')),
                ('cart', models.ManyToManyField(to='cafe.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='deliveryorder',
            name='cart',
            field=models.ManyToManyField(to='cafe.Product'),
        ),
    ]
