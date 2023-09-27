from django.urls import path
from .views import usuarios, login, index, camas, cama, detalle, alerta
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [path('', index.as_view(), name='index'),
               path('habitaciones', camas.as_view(), name='lista'),
               path('login/', login.as_view(), name='login'),
               path('salir/', LogoutView.as_view(next_page='login'), name='logout'),
               path('detalle/<int:pk>', detalle.as_view(), name='detalle'),
               path('alerta', alerta.as_view(), name='alerta'),
               path('arduinoalert', views.alertaarduino, name='arduinoalert')]

