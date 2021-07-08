from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList

urlpatterns = [
    
    # localhost:8000/usuario/registrar
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    
    # localhost:8000/usuario/listar
    path('listar', UserList.as_view(), name="list_user"),
]