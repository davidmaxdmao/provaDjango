from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import ClienteFisico
from core.api.serializers import ClienteFisicoSerializer

class ClienteFisicoViewSet(ModelViewSet):
    queryset = ClienteFisico.objects.all()
    serializer_class = ClienteFisicoSerializer

    @action(methods=['get'], detail=False)
    def listar(self, request, *args, **kwargs):
        return super().list(request,*args,**kwargs)

    @action(methods=['post'], detail=False)
    def teste(self, request):
        cpf = request.data['cpf']
        nome = request.data['nome']
        valido = ClienteFisico.api_valida_cpf(cpf)
        context = {'cpf': cpf, 'nome': nome, 'valido': valido}
        return Response(context)