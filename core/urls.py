from django.urls import path, include

from .views import index_view
from .views import cadastrar_cliente_fisico
from .views import cadastrar_cliente_juridico


urlpatterns = [
    path('', index_view, name='index'),
    path('Cadastro/ClienteFisico', cadastrar_cliente_fisico, name='CadastroFisico'),
    path('Cadastro/ClienteJuridico', cadastrar_cliente_juridico, name='CadastroJuridico'),
    path('accounts/', include('accounts.urls')),
]
