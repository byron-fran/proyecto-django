from django.urls import path
from .views import tarea, inicio, ListaPendientes, TareaDetalle, CrearTarea, Editar_tarea, Eliminar, Logeo, PaginaRegistro
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', inicio),
    path('tarea/', tarea),
    path('lista/', ListaPendientes.as_view(), name='pendientes'),
    path('detalle/<int:pk>', TareaDetalle.as_view(), name='detalle'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
    path('editar-tarea/<int:pk>', Editar_tarea.as_view(), name='editar'),
    path('eliminar/<int:pk>', Eliminar.as_view(), name='eliminar'),
    path('login/', Logeo.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name='logout'),
    path('registro/', PaginaRegistro.as_view(), name='registro')


    


]