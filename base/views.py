from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpRequest,StreamingHttpResponse
from .models import alarma,formulario,habitacion,usuarios,cama
from django.contrib.auth.mixins import LoginRequiredMixin

class index(LoginView):
    template_name = "base/login.html"
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lista')

class login(LoginView):
    template_name = "base/login.html"
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lista')
    

class detalle(LoginRequiredMixin, DetailView):
    model = cama
    context_object_name = 'detalles'
    template_name = 'base/detalle.html'
    field = '__all__'

class alerta(CreateView):
    model = alarma
    context_object_name = 'alertas'
    fields = ['activa']
    template_name = 'base/alerta.html'
    success_url = reverse_lazy('lista')


class camas(LoginRequiredMixin, ListView):
    model = cama
    context_object_name = "camas"

def alertaarduino(arduinoalert):
    return HttpResponse('Perro')
    
    

# Create your views here.
