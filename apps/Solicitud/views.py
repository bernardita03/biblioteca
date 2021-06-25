from django.shortcuts import render
from .models import Solicitud
from .forms import SolicitudForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# para la clase generics
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# Create your views here.
def listar_solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, "Solicitud/listar_solicitudes.html", {'solicitudes': solicitudes})

def agregar_solicitud(request):
    if request.method == "POST":
        form = SolicitudForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_solicitud")
    else:
        form = SolicitudForm()
        return render(request, "Solicitud/agregar_solicitud.html", {'form': form})

def borrar_solicitud(request, solicitud_id):
    instancia = Solicitud.objects.get(id=solicitud_id)
    instancia.delete()
    return redirect('listar_solicitudes')

def borrar_solicitud(request, solicitud_id):
    instancia = Solicitud.objects.get(id=solicitud_id)
    instancia.delete()
    return redirect('listar_solicitudes')

def editar_solicitud(request, solicitud_id):
    instancia = solicitud.objects.get(id=solicitud_id)
    form = SolicitudForm(instance=instancia)
    if request.method == "POST":
        form = SolicitudForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "Solicitud/editar_solicitud.html", {'form': form})

#clases

class SolicitudCreate(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'Solicitud/agregar_solicitud.html'
    success_url = reverse_lazy("listar_solicitudes")
    
    
class SolicitudList(ListView):
    model = Solicitud
    template_name = 'Solicitud/list_solicitudes.html'
    # paginate_by = 4

class SolicitudUpdate(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'Solicitud/solicitud_form.html'
    success_url = reverse_lazy('list_solicitud')

class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'Solicitud/solicitud_delete.html'
    success_url = reverse_lazy('list_solicitud')



