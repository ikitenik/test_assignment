from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ..views import CashFlowViewSet


app_name = 'cash_flow'

router = SimpleRouter()
router.register('cash-flow', CashFlowViewSet, basename='cash_flow')

main_urls = [
    path('', include(router.urls)),
]
