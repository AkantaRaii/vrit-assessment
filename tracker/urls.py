from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import *

router=DefaultRouter()
router.register(r'expense', ExpenseIncomeViewSet, basename='expense')

urlpatterns=[
    path('', include(router.urls)),
    path('auth/register/', register_user, name='register'),
]