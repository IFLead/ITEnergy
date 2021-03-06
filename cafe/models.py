from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from ITEnergy import bot


class Product(models.Model):
    name = models.CharField('Название', max_length=64)
    name_id = models.CharField('Название, латиницей', max_length=64, unique=True)
    price = models.DecimalField('Стоимость', max_digits=6, decimal_places=0)
    image = models.ImageField(upload_to='static/images/coffee_types', null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    name = models.CharField('Имя заказчика', max_length=128)
    tel_number = models.CharField('Номер телефона', max_length=25)

    class Meta:
        abstract = True



class Employee(models.Model):
    name = models.CharField('ФИО', max_length=128)
    chat_id = models.CharField('ID Telegram', max_length=32, unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True



class DeliveryOrder(Order):
    address = models.CharField('Адрес', max_length=128)
    date_ordered = models.DateTimeField('Дата заказа', null=False, blank=False)
    total_price = models.PositiveIntegerField('Общая сумма', default=0)
    declined_by = models.ManyToManyField('DeliveryStaff')

    def save(self, *args, **kw):
        sum = 0
        for i in self.item_set.all():
            sum += i.price
        self.total_price = sum
        super(DeliveryOrder, self).save(*args, **kw)

    def __str__(self):
        return 'Для {} от {} '.format(self.name, self.date_ordered.strftime("%d.%m.%Y %H:%M:%S"))

    class Meta:
        verbose_name = 'Заказ на доставку'
        verbose_name_plural = 'Заказы на доставку'


class Item(models.Model):
    order = models.ForeignKey(DeliveryOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False)

    quantity = models.PositiveIntegerField('Количество')
    price = models.PositiveIntegerField('Сумма', default=0)

    def save(self, *args, **kw):
        self.price = int(self.quantity * self.product.price)
        super(Item, self).save(*args, **kw)

    def __str__(self):
        return '{} {}'.format(self.quantity, self.product.name)

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'



class DeliveryStaff(Employee):
    actual_order = models.OneToOneField(DeliveryOrder, null=True, blank=True)
    orders_count = models.PositiveIntegerField('Заказов получено' ,default=0)
    orders_decline = models.PositiveIntegerField('Заказов отказано' ,default=0)

    def save(self, *args, **kw):
        if self.pk is not None:
            orig = DeliveryStaff.objects.get(pk=self.pk)
            if orig.is_verified != self.is_verified:
                if self.is_verified:
                    bot.send_message(chat_id=self.chat_id,
                                     text='Ваш статус подтвержден')
                else:
                    bot.send_message(chat_id=self.chat_id,
                                     text='Ваш статус аннулирован')
        super(DeliveryStaff, self).save(*args, **kw)

    class Meta:
        verbose_name = 'Служба доставки'
        verbose_name_plural = 'Служба доставки'


class ReservationOrder(Order):
    date_visit = models.DateTimeField()
    count_visitors = models.PositiveSmallIntegerField('Количество посетителей')
    number_place = models.PositiveSmallIntegerField('Номер стола')

    def __str__(self):
        return 'В {} на {}, место #{} '.format(self.date_visit.strftime("%d.%m.%Y %H:%M:%S"), self.count_visitors,
                                               self.number_place)

    class Meta:
        verbose_name = 'Заявка на бронирование'
        verbose_name_plural = 'Заявки на бронирование'