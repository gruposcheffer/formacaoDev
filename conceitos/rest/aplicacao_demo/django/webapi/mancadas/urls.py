from django.urls import path, include
from rest_framework import routers
from .views import IndividuoViewSet, MancadaViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register('individuos', IndividuoViewSet)
router.register('mancadas', MancadaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
