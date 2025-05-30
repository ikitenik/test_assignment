from rest_framework import viewsets
from ..models import (
    StatusReference,
    TypeReference,
    CategoryReference,
    SubcategoryReference,
)
from ..serializers import (
    StatusSerializer,
    TypeSerializer,
    CategorySerializer,
    SubcategorySerializer,
)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = StatusReference.objects.all()
    serializer_class = StatusSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = TypeReference.objects.all()
    serializer_class = TypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryReference.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = SubcategoryReference.objects.all()
    serializer_class = SubcategorySerializer
