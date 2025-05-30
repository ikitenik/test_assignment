from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from ..models import CashFlowModel
from ..serializers import CashFlowSerializer
from ..services import FilterService

from datetime import date


class CashFlowViewSet(viewsets.ModelViewSet):
    queryset = CashFlowModel.objects.all()
    serializer_class = CashFlowSerializer

    def get_queryset(self):
        """Изменяем queryset при фильтрации"""
        self.queryset = self.queryset.all()
        if self.action == "list":
            self.queryset = FilterService.filter_queryset(
                self.queryset,
                self.request.query_params)
        return self.queryset

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if not data.get('date_create', None):
            data['date_create'] = str(date.today())
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)