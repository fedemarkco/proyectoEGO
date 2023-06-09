from django.urls import include, path
from rest_framework import routers

from .views import ModelCarsViewSet, ModelSheetViewSet

router = routers.DefaultRouter()
router.register(r"model-cars", ModelCarsViewSet, basename="model-cars")
router.register(r"model-sheet", ModelSheetViewSet, basename="model-sheet")

urlpatterns = [
    path("", include(router.urls))
]
