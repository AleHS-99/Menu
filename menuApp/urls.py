"""menu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', HomePage.as_view(),name='Home'),
    path('qr/',qrcode2,name='generar'),
    path('abaut/',abaut,name='abaut'),
    path('accounts/login/',LoginFormView.as_view(),name='login'),
    path('login/',LoginFormView.as_view(),name='login'),
    path('logout',LogoutView.as_view(), name='logout'),
    path('listar/ofertas/',ofertas.as_view(),name='addO'),
    path('listar/servicios/',Servicios.as_view(),name='addS'),
    path('listar/ofertas/Add',AddOferta.as_view(),name='addOa'),
    path('listar/servicios/Add',AddServicio.as_view(),name='addSa'),
    path('listar/ofertas/Editar/<int:pk>/',update,name='editarA'),
    path('listar/servicios/Editar/<int:pk>/',updateS,name='editarS'),
    path('listar/ofertas/Delete/<int:pk>/',DeleteCola.as_view(),name='deletea'),
    path('listar/servicios/Delete/<int:pk>/',DeleteS.as_view(),name='deletes'),
    path('register', CreateUserForm.as_view(), name='register'),
]
