from django.db import models


class ReferenceBaseModel(models.Model):
    """
    Базовый класс для справочников.
    """
    title = models.CharField(max_length=255, unique=True, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class StatusReference(ReferenceBaseModel):
    """
    Справочник статусов
    """

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class TypeReference(ReferenceBaseModel):
    """
    Справочник типов
    """

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class CategoryReference(ReferenceBaseModel):
    """
    Справочник категорий
    """
    # Привязываем категорию к типу
    type = models.ForeignKey(
        TypeReference,
        on_delete=models.CASCADE,
        verbose_name='Тип')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubcategoryReference(ReferenceBaseModel):
    """
    Справочник подкатегорий
    """
    # Привязываем подкатегорию к категории
    category = models.ForeignKey(
        CategoryReference,
        on_delete=models.CASCADE,
        verbose_name='Категория')

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"





