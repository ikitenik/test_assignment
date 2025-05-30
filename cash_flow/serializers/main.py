from rest_framework import serializers
from ..models import CashFlowModel


class CashFlowSerializer(serializers.ModelSerializer):
    # Наименование статуса
    status_title = serializers.CharField(source="status.title",
                                         read_only=True, default="")
    # Наименование типа
    type_title = serializers.CharField(source="type.title",
                                       read_only=True, default="")
    # Наименование категории
    category_title = serializers.CharField(source="category.title",
                                           read_only=True, default="")
    # Наименование подкатегории
    subcategory_title = serializers.CharField(source="subcategory.title",
                                              read_only=True, default="")

    class Meta:
        model = CashFlowModel
        fields = '__all__'
