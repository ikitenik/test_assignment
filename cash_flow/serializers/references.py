from rest_framework import serializers
from ..models import (
    StatusReference,
    TypeReference,
    CategoryReference,
    SubcategoryReference,
)


class StatusSerializer(serializers.ModelSerializer):
    """Сериализатор справочника статусов"""
    class Meta:
        model = StatusReference
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    """Сериализатор справочника типов"""
    class Meta:
        model = TypeReference
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор справочника категорий"""
    class Meta:
        model = CategoryReference
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор справочника подкатегорий"""
    class Meta:
        model = SubcategoryReference
        fields = '__all__'
