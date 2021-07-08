from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import LibroList, DocenteCreate, LibroUpdate , LibroDelete
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Libro import views

urlpatterns = [
    path('listar/', LibroList.as_view(), name="libros_list"),
    path('crear/', LibroCreate.as_view(), name="libros_form"),
    path('editar/<int:pk>', LibroUpdate.as_view(), name="libros_update"),
    path('borrar/<int:pk>', LibroDelete.as_view(), name="libros_borrar"),
    
]

urlpatterns += [
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)