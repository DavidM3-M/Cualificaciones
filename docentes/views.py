from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    Person,
    InformacionContacto,
    Documento,
    Estudio,
    Experiencia,
    ProduccionAcademica,
    DocumentoSoporte,
)
from .serializers import (
    PersonSerializer,
    InformacionContactoSerializer,
    DocumentoSerializer,
    EstudioSerializer,
    ExperienciaSerializer,
    ProduccionAcademicaSerializer,
    DocumentoSoporteSerializer,
)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer



class InformacionContactoViewSet(viewsets.ModelViewSet):
    queryset = InformacionContacto.objects.all()
    serializer_class = InformacionContactoSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class EstudioViewSet(viewsets.ModelViewSet):
    queryset = Estudio.objects.all()
    serializer_class = EstudioSerializer


class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer


class ProduccionAcademicaViewSet(viewsets.ModelViewSet):
    queryset = ProduccionAcademica.objects.all()
    serializer_class = ProduccionAcademicaSerializer


class DocumentoSoporteViewSet(viewsets.ModelViewSet):
    queryset = DocumentoSoporte.objects.all()
    serializer_class = DocumentoSoporteSerializer
# Create your views here.
