from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('avia', FlightListCreateView, basename='avia')

urlpatterns = [
    path('', include(router.urls)),
    path('avia', FlightListCreateView.as_view()),
]