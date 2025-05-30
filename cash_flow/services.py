from rest_framework.exceptions import ValidationError


class FilterService:
    @staticmethod
    def filter_queryset(queryset, query_params):
        """Функция фильтрует данные при наличии query-param фильтрации"""
        # Фильтрация по дате (Начиная с даты)
        if date_start := query_params.get('date1', None):
            queryset = queryset.filter(date_create__gte=date_start)
        # Фильтрация по дате (заканчивая датой)
        if date_end := query_params.get('date2', None):
            queryset = queryset.filter(date_create__lte=date_end)
        # Фильтрация по статусу
        if status := query_params.get('status', None):
            queryset = queryset.filter(status__title=status)
        # Фильтрация по типу
        if type := query_params.get('type', None):
            queryset = queryset.filter(type__title=type)
        # Фильтрация по категории
        if category := query_params.get('category', None):
            queryset = queryset.filter(category__title=category)
        # Фильтрация по подкатегории
        if subcategory := query_params.get('subcategory', None):
            queryset = queryset.filter(subcategory__title=subcategory)

        return queryset


class ValidateService:
    @staticmethod
    def validate_cash_flow(cash_flow_object):
        """Функция проверяет корректность выбранных категорий и подкатегорий"""
        ValidateService._validate_category(cash_flow_object)
        ValidateService._validate_subcategory(cash_flow_object)

    @staticmethod
    def _validate_category(cash_flow_object):
        """Функция проверяет, относится ли выбранная категория
        к выбранному типу"""
        if cash_flow_object.type != cash_flow_object.category.type:
            raise ValidationError({"category": "Категория должна относиться "
                                   "к выбранному типу."})

    @staticmethod
    def _validate_subcategory(cash_flow_object):
        """Функция проверяет, относится ли выбранная подкатегория
        к выбранной категории"""
        if cash_flow_object.category != cash_flow_object.subcategory.category:
            raise ValidationError({"subcategory":
                                   "Подкатегория должна относиться "
                                   "к выбранной категории."})
