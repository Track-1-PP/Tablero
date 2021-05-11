from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import EntrevistadorForm
from .forms import EntrevistadoForm
from .forms import EmpresaForm
from .models import Agendar
from .forms import AgendarForm

#Formularios en html

def signin(request):
		submitted = False
		if request.method == "POST":
				form = EntrevistadorForm(request.POST)
				if form.is_valid():
						form.save()
						return HttpResponseRedirect('/signin?submitted=True')
		else:
				form = EntrevistadorForm
				if 'submitted' in request.GET:
						submitted = True

		return render(request, 'inicio/signin.html', {
			'form': form, 'submitted':submitted
		})


def inicio(request):
		return render(request,'inicio/inicio.html',
      {

      })


def empresa(request):
		submitted = False
		if request.method == "POST":
			form = EmpresaForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('empresa?submitted=True')
		else:
			form = EmpresaForm
			if 'submitted' in request.GET:
				submitted = True
				
		return render(request, 'inicio/empresa.html', {
			'form': form, 'submitted':submitted
		})


def agenda(request):
	submitted = False
	if request.method == "POST":
		form = AgendarForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/miusuario_entrevistador/')

	else:
		form = AgendarForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request,'agenda/agenda.html', {
		'form': form, 'submitted':submitted
	})








def videollamada(request):
    return render(request,
     'videollamada/videollamada.html',
      {

      })


def register_entrevistador(request):
		submitted = False
		if request.method == "POST":
				form = EntrevistadorForm(request.POST)
				if form.is_valid():
						form.save()
						return HttpResponseRedirect('/signin?submitted=True')
		else:
				form = EntrevistadorForm
				if 'submitted' in request.GET:
						submitted = True

		return render(request, 'inicio/register_entrevistador.html', {
			'form': form, 'submitted':submitted
		})




def register_postulante(request):
		submitted = False
		if request.method == "POST":
				form = EntrevistadoForm(request.POST)
				if form.is_valid():
						form.save()
						return HttpResponseRedirect('/signin?submitted=True')
		else:
				form = EntrevistadoForm
				if 'submitted' in request.GET:
						submitted = True

		return render(request, 'inicio/register_postulante.html', {
			'form': form, 'submitted':submitted
		})


def miUsuario(request):
    return render(request,
     'miUsuario/miUsuario.html',
      {

      })
  
def ambienteProgramacion(request):
  return render (request,
  "ambienteProgramacion/ambienteProgramacion.html",
  {})

def ambientePizarra(request):
  return render (request,
  "ambientePizarra/ambientePizarra.html",
  {})

def miUsuarioEntrevistador(request):
  return render (request,
    'miUsuarioEntrevistador/miUsuarioEntrevistador.html',
    {

    })