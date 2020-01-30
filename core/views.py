from django.shortcuts import render, redirect
from .models import Cliente, ClienteFisico, ClienteJuridico

from .forms import ClienteFisicoForm
from .forms import ClienteJuridicoForm
from .forms import ClienteForm
# Create your views here.

def index_view(request):

    cliente_fisico = ClienteFisicoForm()
    cliente_juridico = ClienteJuridicoForm()
    context = {
        'cliente_fisico':cliente_fisico,
        'cliente_juridico':cliente_juridico,
    }

    return render(request, 'index.html', context)



def cadastrar_cliente_fisico(request):

    if request.method == 'POST':
        cliente_fisico = ClienteFisicoForm(request.POST)


        if cliente_fisico.is_valid():

            nome = cliente_fisico.cleaned_data['nome']
            cpf = cliente_fisico.cleaned_data['cpf']

            if cliente_fisico.valida_nome(nome, request) and cliente_fisico.valida_cpf(cpf, request):
                return redirect('index')
            else:
                cliente_juridico = ClienteJuridicoForm()
                return render(request, 'index.html', {'cliente_fisico': cliente_fisico, 'cliente_juridico':cliente_juridico})



def cadastrar_cliente_juridico(request):

    if request.method == 'POST':
        cliente_juridico = ClienteJuridicoForm(request.POST)

        if cliente_juridico.is_valid():

            nome = cliente_juridico.cleaned_data['nome']
            cnpj = cliente_juridico.cleaned_data['cnpj']

            if cliente_juridico.valida_nome(nome, request) and cliente_juridico.valida_cnpj(cnpj, request):
                return redirect('index')
            else:
                cliente_fisico = ClienteFisicoForm()
                return render(request, 'index.html', {'cliente_juridico': cliente_juridico, 'cliente_fisico':cliente_fisico})

