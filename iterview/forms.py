from django import forms
from django.forms import ModelForm
from .models import Entrevistado, Entrevistador, Agendar, Reunion, Empresa

#Formularios para ingresar los datos a la BBDD

#Formulario Empresa
#Las empresas nuevas se deben agregar maualmentee desde la pagina de /admin, no ha sido creada la pagina donde se rellena el formulario para nuevas empresas
class EmpresaForm(ModelForm):
	class Meta: 
			model = Empresa
			fields = ('nombre_empresa',)

			widgets = {
				'nombre_empresa': forms.TextInput(attrs ={'class' : 'form-control'}),
			}

#Entrevistado 
#Formulario para registrar a nuevos usuarios postulantes
class EntrevistadoForm(ModelForm):
  class Meta:
			model = Entrevistado
			fields = ('nombre', 'apellido', 'email', 'contraseña',)

			widgets = {
				'nombre': forms.TextInput(attrs ={'class' : 'form-control'}),
				'apellido': forms.TextInput(attrs ={"class" : "form-control"}),
				'email': forms.EmailInput(attrs ={"class" : "form-control"}),
				'contraseña': forms.PasswordInput(attrs ={"class" : "form-control"}),

			}

#Entrevistado Sign in
#Formulario para que el entrevistado ingresar a la pagina
#no ha sido implementado el formulario al template en html
class EntrevistadoSign(ModelForm):
  class Meta:
			model = Entrevistado
			fields = ('email', 'contraseña',)

			widgets = {
				'email': forms.EmailInput(attrs ={"class" : "form-control"}),
				'contraseña': forms.PasswordInput(attrs ={"class" : "form-control"}),
			}

#Entrevistador
#Formulario para registrar a nuevos trabajadores de una empresa
class EntrevistadorForm(ModelForm):
  class Meta:
			model = Entrevistador
			fields = ('nombre', 'apellido', 'email', 'contraseña', 'empresa',)

			widgets = {
				'nombre': forms.TextInput(attrs ={'class' : 'form-control'}),
				'apellido': forms.TextInput(attrs ={"class" : "form-control"}),
				'email': forms.EmailInput(attrs ={"class" : "form-control"}),
				'contraseña': forms.PasswordInput(attrs ={"class" : "form-control"}),
				'empresa': forms.Select(attrs={'class':'form-select'}),
			}

#Entrevistador Sign in
#Formulario para que el entrevistador ingresar a la pagina
#no ha sido implementado el formulario al template en html
class EntrevistadorSign(ModelForm):
  class Meta:
			model = Entrevistador
			fields = ('email', 'contraseña',)

			widgets = {
				'email': forms.EmailInput(attrs ={"class" : "form-control"}),
				'contraseña': forms.PasswordInput(attrs ={"class" : "form-control"}),
			}


#Reunion
#Se debe implementar en la pagina de mi usuario 
class ReunionForm(ModelForm):
	class Meta:
		model = Reunion
		fields = {'cantidad', 'duracion', 'link'}

#Agenda
class AgendarForm(ModelForm):
  class Meta:
			model = Agendar
			fields = ('nombre_agenda', 'fecha', 'entrevistado', 'entrevistador', 'reunion', 'lenguaje_programacion')

			widgets = {
				'nombre_agenda': forms.TextInput(attrs={'class':'form-control'}),
				'fecha': forms.TextInput(attrs={'class':'form-control'}),
				'entrevistado': forms.Select(attrs={'class':'form-select'}),
				'entrevistador': forms.Select(attrs={'class':'form-select'}),
				'reunion': forms.Select(attrs={'class':'form-select'}),
				'lenguaje_programacion': forms.TextInput(attrs={'class':'form-control'}),
			}
