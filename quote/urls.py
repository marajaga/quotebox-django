from django.urls import path, include
from .views import QuoteViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('quotes', QuoteViewSet, basename='quotes')

urlpatterns = [
    path('api/', include(router.urls)),
]