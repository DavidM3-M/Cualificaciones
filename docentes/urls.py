from django.urls import path, include
from rest_framework.routers import DefaultRouter
from docentes.views import PersonViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet)
urlpatterns = [
    path('', include(router.urls)),
]