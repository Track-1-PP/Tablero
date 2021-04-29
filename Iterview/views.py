from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import EntrevistadorForm
from .forms import EntrevistadoForm
from .forms import EmpresaForm

#Funciones que hacen el llamado al template

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
    return render(request,
     'agenda/agenda.html',
      {

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
						return HttpResponseRedirect('/miusuario_entrevistador?submitted=True')
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
						return HttpResponseRedirect('/miusuario?submitted=True')
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

def miUsuario_entrevistador(request):
    return render(request,
     'miUsuario/miUsuarioEntrevistador.html',
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