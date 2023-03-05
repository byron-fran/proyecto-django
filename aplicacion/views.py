from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Actividad
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    lista_frutas = ['manzana', 'pera','uva','sandia', 'melon']

    return render(request, 'index.html',{
        'frutas': lista_frutas
    })
def tarea(request):
    return render(request, 'tarea.html')

class ListaPendientes(LoginRequiredMixin,ListView):
    model = Actividad
    context_object_name = 'actividades'
    template_name = 'aplicacion/tareas.html'
    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['actividades'] = context['actividades'].filter(usuario=self.request.user)
        context['count'] = context['actividades'].filter(completo = False).count()

        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['actividades'] = context['actividades'].filter(titulo__icontains=valor_buscado)
            context['valor_buscado'] = valor_buscado
        return context


class TareaDetalle(LoginRequiredMixin, DetailView):
    model = Actividad
    context_object_name = 'tarea'
    template_name='aplicacion/detalle.html'

class CrearTarea(LoginRequiredMixin,CreateView):
    model = Actividad
    fields = ['titulo','info','completo']
    success_url = reverse_lazy('pendientes')
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)

#este codigo realiza una peticion
class Editar_tarea(LoginRequiredMixin, UpdateView):
    model = Actividad
    fields =  ['titulo','info','completo']
    success_url = reverse_lazy('pendientes')

class Eliminar(LoginRequiredMixin,DeleteView):
    model = Actividad
    context_object_name = 'tareas'
    success_url = reverse_lazy('pendientes')


class Logeo(LoginView):
    template_name ='aplicacion/login.html'
    field = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('pendientes')
    
class PaginaRegistro(FormView):
    template_name = 'aplicacion/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('pendientes')
    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)
    def get(self, *args, **kwargs):
       if self.request.user.is_authenticated:
           return redirect('pendientes')
       return super(PaginaRegistro, self).get(*args, **kwargs)
                



    
   