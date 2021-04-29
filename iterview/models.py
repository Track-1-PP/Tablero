from django.db import models
#Modelos de las clases

#empresa
class Empresa(models.Model):
		nombre_empresa = models.CharField('empresa', max_length=60, default='Nombre Empresa')

		def __str__(self):
			return self.nombre_empresa


#entrevistado
class Entrevistado(models.Model): 
		nombre = models.CharField('nombre', max_length=60)
		apellido = models.CharField('apellido', max_length=60)
		email = models.EmailField('direccion email', max_length=128)
		contraseña = models.CharField('contraseña', max_length=60)

		def __str__(self):
			return self.nombre + ' ' + self.apellido


#entrevistador
class Entrevistador(models.Model): 
		nombre = models.CharField('nombre', max_length=60)
		apellido = models.CharField('apellido', max_length=60)
		rol = models.CharField('rol', max_length=60)
		empresa = models.ForeignKey(Empresa, blank=True, null=True, on_delete=models.DO_NOTHING)
		email = models.EmailField('direccion email', max_length=128)
		contraseña = models.CharField('contraseña', max_length=60)

		def __str__(self):
			return self.nombre


#Reunion
class Reunion(models.Model):
		cantidad = models.PositiveIntegerField()
		duracion = models.PositiveIntegerField()
		link = models.URLField('link reunion', max_length=280, default='ejemplo.com')

		def __str__(self):
			return str(self.cantidad) + ',' + str(self.duracion)

#agendar
class Agendar(models.Model):
		nombre_agenda = models.CharField('nombre', max_length=60, default='pepo')
		fecha = models.DateTimeField('fecha reunion')
		entrevistado = models.ForeignKey(Entrevistado, blank=True, null=True, on_delete=models.DO_NOTHING)
		entrevistador = models.ForeignKey(Entrevistador, blank=True, null=True, on_delete=models.DO_NOTHING)
		reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
		lenguaje_programacion = models.CharField('nombre lenguaje de programacion', max_length=60)

		def __str__(self):
			return str(self.fecha) + ',' + str(self.entrevistado)
