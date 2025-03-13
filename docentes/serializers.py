from rest_framework import serializers
from .models import (
    InformacionContacto,
    Documento,
    Estudio,
    Experiencia,
    ProduccionAcademica,
    DocumentoSoporte,
    Person,
)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'



class InformacionContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacionContacto
        fields = '__all__'


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'


class EstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudio
        fields = '__all__'


class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencia
        fields = '__all__'


class ProduccionAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduccionAcademica
        fields = '__all__'


class DocumentoSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoSoporte
        fields = '__all__'    
    