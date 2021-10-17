
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ShopViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r"/shop", ShopViewSet,basename="shop")

urlpatterns = router.urls
