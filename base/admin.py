from django.contrib import admin
from .models import usuarios,alarma,formulario,habitacion,cama

admin.site.register(usuarios)
admin.site.register(formulario)
admin.site.register(alarma)
admin.site.register(cama)
admin.site.register(habitacion)

# Register your models here.
