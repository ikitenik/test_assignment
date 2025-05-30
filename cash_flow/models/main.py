from django.db import models
from .references import (
    StatusReference,
    TypeReference,
    CategoryReference,
    SubcategoryReference,
)

from django.core.validators import MinValueValidator
from ..services import ValidateService


class CashFlowModel(models.Model):
    date_create = models.DateField(
        verbose_name='Дата создания ДДС')

    status = models.ForeignKey(
        StatusReference,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name='Статус')

    type = models.ForeignKey(
        TypeReference,
        on_delete=models.CASCADE,
        verbose_name='Тип')

    category = models.ForeignKey(
        CategoryReference,
        on_delete=models.CASCADE,
        verbose_name='Категория')

    subcategory = models.ForeignKey(
        SubcategoryReference,
        on_delete=models.CASCADE,
        verbose_name='Подкатегория')

    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), ],
        verbose_name='Сумма')

    note = models.TextField(default='', blank=True, null=True,
                            verbose_name='Комментарий')

    class Meta:
        verbose_name = "Движение денежных средств"
        verbose_name_plural = "Движения денежных средств"

    def save(self, *args, **kwargs):
        ValidateService.validate_cash_flow(self)
        super().save(*args, **kwargs)
