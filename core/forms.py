from django import forms
from .models import ClienteFisico
from .models import ClienteJuridico
from .models import Cliente

from django.contrib import messages
import re
from pycpfcnpj import cpfcnpj




class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def valida_nome(self, nome, request):
        valida = re.findall('[^A-Za-z ]', nome)
        if valida:
            messages.error(request, 'Nome invalido, o nome não pode conter numeros ou caracteres especiais!')
            return False
        else:
            messages.success(request, 'nome valido')
            return True


class ClienteFisicoForm(ClienteForm, forms.ModelForm):

    # data_cadastro = forms.DateField(input_formats=['%d/%m/%Y'])

    class Meta:
        model = ClienteFisico
        fields = '__all__'


    def valida_cpf(self, cpf, request):

        # verifica se há letras no cpf
        cpf_sem_letras = not re.findall('[A-Za-z]', cpf)

        if cpfcnpj.validate(cpf) and cpf_sem_letras:
            messages.success(request, 'cpf valido')
            return True
        else:
            messages.error(request, 'cpf invalido, digite um cpf existente/real, somente numeros ou numeros e pontos')
            return False




class ClienteJuridicoForm(ClienteForm, forms.ModelForm):

    class Meta:
        model = ClienteJuridico
        fields = '__all__'


    def valida_cnpj(self, cnpj, request):

        # verifica se há letras no cpf
        cnpj_sem_letras = not re.findall('[A-Za-z]', cnpj)

        if cpfcnpj.validate(cnpj) and cnpj_sem_letras:
            messages.success(request, 'cnpj valido')
            return True
        else:
            messages.error(request, 'cnpj invalido, digite um cnpj existente/real, somente numeros ou numeros e pontos')
            return  False

