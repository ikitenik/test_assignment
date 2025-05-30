from django.contrib import admin
from .models import (
    CashFlowModel,
    StatusReference,
    TypeReference,
    CategoryReference,
    SubcategoryReference,
)


admin.site.register(CashFlowModel)
admin.site.register(StatusReference)
admin.site.register(TypeReference)
admin.site.register(CategoryReference)
admin.site.register(SubcategoryReference)

