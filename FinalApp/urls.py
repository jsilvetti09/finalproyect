from django import views
from django.urls import path
from .views import ComputadoraCreacion, HomeView, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, PcsLista, PcsDetalle, PcsUpdate, PcsDelete, NotebookLista, NotebookDetalle, NotebookDelete, NotebookUpdate, NetbookLista, NetbookDetalle, NetbookUpdate, NetbookDelete, OtroLista, OtroDetalle, OtroUpdate, OtroDelete, ComentarioPagina  
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('accounts/login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(template_name='registro.html'), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaPcs/', PcsLista.as_view(), name='Pcs'),
    path('listaNotebooks/', NotebookLista.as_view(), name='Notebook'),
    path('listaNetbooks/', NetbookLista.as_view(), name='Netbook'),
    path('listaOtros/', OtroLista.as_view(), name='otros'),

    path('PcsDetalle/<int:pk>/', PcsDetalle.as_view(), name='Pcs'),
    path('NotebookDetalle/<int:pk>/', NotebookDetalle.as_view(), name='Notebook'),
    path('NetbookDetalle/<int:pk>/', NetbookDetalle.as_view(), name='Netbook'),
    path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),

    path('PcsEdicion/<int:pk>/', PcsUpdate.as_view(), name='Pcs_editar'),
    path('NotebookEdicion/<int:pk>/', NotebookUpdate.as_view(), name='Notebook_editar'),
    path('NetbookEdicion/<int:pk>/', NetbookUpdate.as_view(), name='Netbook_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),


    path('PcsBorrado/<int:pk>/', PcsDelete.as_view(), name='Pcs_eliminar'),
    path('NotebookBorrado/<int:pk>/', NotebookDelete.as_view(), name='Notebook_eliminar'),
    path('NetbookBorrado/<int:pk>/', NetbookDelete.as_view(), name='Netbook_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('ComputadoraCreacion/', ComputadoraCreacion.as_view(), name='nuevo'),

    path('PcsDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('NotebookDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('NetbookDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
    
    
    
    
]
