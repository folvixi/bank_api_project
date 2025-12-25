from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, LoanViewSet, DepositViewSet

# создаем роутер для автоматических URL
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'deposits', DepositViewSet)

urlpatterns = [
    path('', include(router.urls)),
]