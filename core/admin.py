from django.contrib import admin
from .models import ClienteFisico
from .models import ClienteJuridico

# Register your models here.
admin.site.register(ClienteFisico)
admin.site.register(ClienteJuridico)