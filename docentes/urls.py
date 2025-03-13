from django.urls import path, include
from rest_framework.routers import DefaultRouter
from docentes.views import (
    PersonViewSet,
    InformacionContactoViewSet,
    DocumentoViewSet,
    EstudioViewSet,
    ExperienciaViewSet,
    ProduccionAcademicaViewSet,
    DocumentoSoporteViewSet,
)


router = DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'contactos', InformacionContactoViewSet)
router.register(r'documentos', DocumentoViewSet)
router.register(r'estudios', EstudioViewSet)
router.register(r'experiencias', ExperienciaViewSet)
router.register(r'producciones', ProduccionAcademicaViewSet)
router.register(r'documentos_soporte', DocumentoSoporteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
