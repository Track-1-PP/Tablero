from .models import Agendar
from .forms import AgendarForm
from .forms import EmpresaForm
from .forms import NewUserForm
from django.contrib import messages
from django.core import serializers
from .forms import EntrevistadoForm
from .forms import EntrevistadorForm
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


#Formularios en html

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("miUsuario")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="inicio/signin.html", context={"login_form":form})

def logout_request(request):
    	logout(request)
    	return redirect('inicio')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="inicio/register_entrevistador.html", context={"register_form":form})

def register_postulante(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="inicio/register_postulante.html", context={"register_form":form})

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

	else:
		form = AgendarForm
		if 'submitted' in request.GET:
			submitted = True

	
	eventos = Agendar.objects.all()
	return render(request,'agenda/agenda.html', {'form': form, 'submitted':submitted, 'eventos':eventos})

def deleteAgenda(request, pk):
	evento = Agendar.objects.get(id=pk)
	if request.method == "POST":
		evento.delete()
		return redirect('/agenda', foo='bar')
	context = {'item':evento}
	return render(request, 'agenda/delete_agenda.html', context)

def updateAgenda(request, pk):

	evento = Agendar.objects.get(id=pk)
	form = AgendarForm(instance=evento)

	if request.method == 'POST':
		form = AgendarForm(request.POST, instance=evento)
		if form.is_valid():
			form.save()
			return redirect('/agenda', foo='bar')

	context = {'form':form}
	return render(request, 'agenda/agenda_form.html', context)


def videollamada(request):
    return render(request,
     'videollamada/videollamada.html',
      {

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