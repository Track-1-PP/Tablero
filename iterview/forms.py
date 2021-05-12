from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Entrevistado, Entrevistador, Agendar, Reunion, Empresa

#Ingresa los datos a la BBDD


#Empresa
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ('nombre_empresa', )

        widgets = {
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
        }


#Entrevistado
class EntrevistadoForm(ModelForm):
    class Meta:
        model = Entrevistado
        fields = (
            'nombre',
            'apellido',
            'email',
            'contraseña',
        )

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'contraseña': forms.PasswordInput(attrs={"class": "form-control"}),
        }


#Entrevistador
class EntrevistadorForm(ModelForm):
    class Meta:
        model = Entrevistador
        fields = (
            'nombre',
            'apellido',
            'email',
            'contraseña',
        )

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'contraseña': forms.PasswordInput(attrs={"class": "form-control"}),
        }


#Reunion
class ReunionForm(ModelForm):
    class Meta:
        model = Reunion
        fields = {'cantidad', 'duracion', 'link'}

#Agenda
class AgendarForm(ModelForm):
    class Meta:
        model = Agendar
        fields = ('nombre_agenda', 'fecha', 'lenguaje_programacion')

        widgets = {
            'nombre_agenda': forms.TextInput(attrs={'class': 'form-control'}),
            'lenguaje_programacion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),

        }

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
    #name = forms.CharField(Required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user