from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class Contract(models.Model):
    producer = models.ForeignKey(
        Producer,
        related_name='contracts',
        on_delete=models.PROTECT,
        verbose_name='Изготовитель'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class Product(models.Model):
    producer = models.ForeignKey(
        Producer,
        related_name='products',
        on_delete=models.PROTECT,
        verbose_name='Изготовитель'
    )
    contract = models.ForeignKey(
        Contract,
        related_name='products',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class LoanApplication(models.Model):
    loaner = models.CharField(max_length=255, verbose_name='Заемщик')
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT, verbose_name='Контракт')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
