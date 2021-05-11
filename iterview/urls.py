from django.urls import path, include
from. import views

#rutas para la URL (ejemplo: "pepo.cl/inicio")

urlpatterns = [
    path('', views.inicio, name="inicio"),
		path('register_postulante/', views.register_postulante, name="register_postulante"),
		path('register_entrevistador/', views.register_entrevistador, name="register_entrevistador"),
		path('signin/', views.signin, name="signin"),
		path('videollamada/', views.videollamada, name="videollamada"),
		path('agenda/', views.agenda, name="agenda"),
		path('delete_agenda/<str:pk>/', views.deleteAgenda, name="delete_agenda"),
		path('miusuario/', views.miUsuario, name="miUsuario"),
        path("miusuario_entrevistador/", views.miUsuarioEntrevistador, name="miUsuarioEntrevistador"),
        path("ambienteprogramacion/", views.ambienteProgramacion, name="ambienteProgramacion"),
        path("ambientepizarra/", views.ambientePizarra, name="ambientePizarra"),
    ]
