from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ..views import (
    StatusViewSet,
    TypeViewSet,
    CategoryViewSet,
    SubcategoryViewSet,
)

app_name = 'cash_flow'

router = DefaultRouter()
router.register(r'status', StatusViewSet, basename='status')
router.register(r'type', TypeViewSet, basename='type')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'subcategory', SubcategoryViewSet, basename='subcategory')

references_urls = [
    path('cash-flow/references/', include(router.urls)),
]
