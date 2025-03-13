from django.db import models

# Create your models here.

class Person(models.Model):
    nro_de_cedula = models.CharField(max_length=20)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20)
    pais_de_residencia = models.CharField(max_length=20)
    departamento_de_residencia = models.CharField(max_length=20)
    ciudad_de_residencia = models.CharField(max_length=50)
    barrio_de_residencia = models.CharField(max_length=20)
    direccion_de_residencia = models.CharField(max_length=100)

class User(models.Model):
    def iniciar_sesion(self):
        pass

    def cerrar_sesion(self):
        pass


class InformacionContacto(models.Model):
    pais_info = models.CharField(max_length=50)
    departamento_info = models.CharField(max_length=50)
    ciudad_info = models.CharField(max_length=50)
    direccion_info = models.CharField(max_length=50)
    barrio_info = models.CharField(max_length=50)
    telefono_fijo = models.CharField(max_length=50, blank=True, null=True)
    telefono_celular = models.CharField(max_length=50)
    correo_electronico = models.EmailField(max_length=50)


class Documento(models.Model):
    fecha_actualizacion_doc = models.DateTimeField()


class Estudio(models.Model):
    tipo_de_estudio = models.CharField(max_length=50)
    graduado = models.BooleanField()
    fecha_de_graduacion = models.DateField()
    institucion_estudio = models.CharField(max_length=50)
    titulo_obtenido = models.CharField(max_length=50)
    titulo_convalidado = models.CharField(max_length=50)
    fecha_de_convalidacion = models.DateField(blank=True, null=True)
    resolucion_de_convalidacion = models.CharField(max_length=50, blank=True, null=True)
    pais_estudio = models.CharField(max_length=50)
    departamento_estudio = models.CharField(max_length=50)
    ciudad_estudio = models.CharField(max_length=50)
    fecha_de_inicio_est = models.DateField()
    fecha_de_finalizacion_est = models.DateField()
    certificado_est = models.BinaryField()


class DocumentoSoporte(models.Model):
    documento_identidad = models.BinaryField()
    tarjeta_servicio_militar = models.BinaryField()


class ProduccionAcademica(models.Model):
    tipo_de_produccion = models.CharField(max_length=50)
    titulo_de_produccion = models.CharField(max_length=50)
    autores = models.CharField(max_length=50)
    fecha_de_publicacion = models.DateField()
    indexada_de = models.CharField(max_length=50)
    base_de_datos = models.CharField(max_length=50)
    institucion_pit = models.CharField(max_length=50)
    pais_pit = models.CharField(max_length=50)
    departamento_pit = models.CharField(max_length=50)
    ciudad_pit = models.CharField(max_length=50)
    tipo_de_participacion = models.CharField(max_length=50)
    archivo_de_produccion = models.BinaryField()


class Experiencia(models.Model):
    tipo_de_experiencia = models.CharField(max_length=50)
    experiencia_ottenida = models.CharField(max_length=50)
    institucion_exp = models.CharField(max_length=100)
    trabajo_actual = models.BooleanField()
    cargo = models.CharField(max_length=50)
    intensidad = models.CharField(max_length=50)
    fecha_de_inicio_exp = models.DateField()
    fecha_de_finalizacion_exp = models.DateField()
    certificado_exp = models.BinaryField()


class Rol(models.Model):
    def visualizar_datos(self):
        pass

    def subir_datos(self):
        pass

    def descargar_datos_pdf(self):
        pass


class Docente(models.Model):
    def modificar_datos(self):
        pass

    def eliminar_datos(self):
        pass


class ApoyoProfesoral(models.Model):
    def actualizar_estadod(self):
        pass

    def filtrar_busqueda(self):
        pass