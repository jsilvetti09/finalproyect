from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Computadora, Comentario
from .forms import ActualizacionComputadora, FormularioCambioPassword, FormularioEdicion, FormularioNuevoComputadora, FormularioRegistroUsuario, FormularioComentario
from django.urls import path

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    
class LoginPagina(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    success_message = "¡Bienvenido!"
    
    def get_success_url(self):
        return reverse_lazy('home')
    


class RegistroPagina(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'passwordExitoso.html', {})


# Pcs

class PcsLista( ListView):
    context_object_name = 'pcs'  
    queryset = Computadora.objects.filter(computadora__startswith='pcs')
    template_name = 'listaPcs.html'
    login_url = '/login/'

class PcsDetalle(DetailView):
    model = Computadora
    context_object_name = 'pcs'
    template_name = 'PcsDetalle.html'

class PcsUpdate(LoginRequiredMixin, UpdateView):
    model = Computadora
    form_class = ActualizacionComputadora
    success_url = reverse_lazy('Pcs')
    context_object_name = 'Pcs'
    template_name = 'PcsEdicion.html'

class PcsDelete(LoginRequiredMixin, DeleteView):
    model = Computadora
    success_url = reverse_lazy('Pcs')
    context_object_name = 'pcs'
    template_name = 'PcsBorrado.html'

#Notebook

class NotebookLista(ListView):
    context_object_name = 'Notebook'
    queryset = Computadora.objects.filter(computadora__startswith='Notebook')
    template_name = 'listaNotebooks.html'

class NotebookDetalle(DetailView):
    model = Computadora
    context_object_name = 'Notebook'
    template_name = 'NotebookDetalle.html'

class NotebookUpdate(LoginRequiredMixin, UpdateView):
    model = Computadora
    form_class = ActualizacionComputadora
    success_url = reverse_lazy('Notebook')
    context_object_name = 'Notebook'
    template_name = 'NotebookEdicion.html'

class NotebookDelete(LoginRequiredMixin, DeleteView):
    model = Computadora
    success_url = reverse_lazy('Notebook')
    context_object_name = 'Notebook'
    template_name = 'NotebookBorrado.html'

# Netbook

class NetbookLista(ListView):
    context_object_name = 'Netbook'
    queryset = Computadora.objects.filter(computadora__startswith='Netbook')
    template_name = 'listaNetbooks.html'

class NetbookDetalle(DetailView):
    model = Computadora
    context_object_name = 'Netbook'
    template_name = 'NetbookDetalle.html'

class NetbookUpdate(LoginRequiredMixin, UpdateView):
    model = Computadora
    form_class = ActualizacionComputadora
    success_url = reverse_lazy('Netbook')
    context_object_name = 'Netbook'
    template_name = 'NetbookEdicion.html'

class NetbookDelete(LoginRequiredMixin, DeleteView):
    model = Computadora
    success_url = reverse_lazy('Netbook')
    context_object_name = 'Netbook'
    template_name = 'NetbookBorrado.html'

# OTRO

class OtroLista(ListView):
    context_object_name = 'otros'
    queryset = Computadora.objects.filter(computadora__startswith='otro')
    template_name = 'listaOtros.html'

class OtroDetalle(DetailView):
    model = Computadora
    context_object_name = 'otros'
    template_name = 'otroDetalle.html'

class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Computadora
    form_class = ActualizacionComputadora
    success_url = reverse_lazy('otros')
    context_object_name = 'otros'
    template_name = 'otroEdicion.html'

class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Computadora
    success_url = reverse_lazy('otros')
    context_object_name = 'otros'
    template_name = 'otroBorrado.html'

# CREACION Computadora

class ComputadoraCreacion(LoginRequiredMixin, CreateView):
    model = Computadora
    form_class = FormularioNuevoComputadora
    success_url = reverse_lazy('home')
    template_name = 'ComputadoraCreacion.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'acercaDeMi.html', {})



# Create your views here.
