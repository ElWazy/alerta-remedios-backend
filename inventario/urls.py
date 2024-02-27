from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inventario import views


router = DefaultRouter()
router.register(r"remedios", views.RemedioViewSet, "remedios")

urlpatterns = [path("", include(router.urls))]
