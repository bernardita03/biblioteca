from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro
from .forms import LibroForm

# API 
from rest_framework import generics
from .serializers import DocenteSerializer
#------------
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings



# ---- API 
class API_objects(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

#----
class LibroList (ListView):                    
    model = Libro
    template_name = 'Libro/libro_list.html'

class LibroCreate (CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'Libro/libro_form.html'
    success_url = reverse_lazy('libros_list')

class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'Libro/libro_form.html'
    success_url = reverse_lazy('libros_list')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'Libro/libro_borrar.html'
    success_url = reverse_lazy('libros_list')
    
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

