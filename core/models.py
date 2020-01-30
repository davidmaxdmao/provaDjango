from django.db import models

from pycpfcnpj import cpfcnpj


class Cliente(models.Model):

    nome = models.CharField('Nome', max_length=100, null=False, blank=False)
    data_cadastro = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome



class ClienteFisico(Cliente):
    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
    ]

    cpf = models.CharField('CPF', max_length=14, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)

    # Esse metodo foi criado para praticar a criação de api's no django
    @staticmethod
    def api_valida_cpf(cpf):
        return cpfcnpj.validate(cpf)



class ClienteJuridico(Cliente):

    cnpj = models.CharField('CNPJ', max_length=18, null=False, blank=False)



