from django.urls import path, include
from . import views
 
urlpatterns = [
 
    
    path('listarSolicitudes', views.listar_solicitudes, name="listar_solicitudes"),

    path('agregar_solicitud', views.agregar_solicitud, name="agregar_solicitud"),

    path('editar_solicitud/<int:solicitud_id>', views.editar_solicitud, name="editar_solicitud"),

    path('borrar_solicitud/<int:solicitud_id>', views.borrar_solicitud, name="borrar_solicitud"),

    # --------------- llamando a la clases --------------------------
    path('add_solicitud', views.SolicitudCreate.as_view(), name="add_solicitud"),

    path('list_solicitud/', views.SolicitudList.as_view(), name='list_solicitud'),

    path('edit_solicitud/<int:pk>', views.SolicitudUpdate.as_view(), name='edit_solicitud'),

    path('del_solicitud/<int:pk>', views.SolicitudDelete.as_view(), name='del_solicitud'),


]
