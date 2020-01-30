from rest_framework.serializers import ModelSerializer
from core.models import ClienteFisico

class ClienteFisicoSerializer(ModelSerializer):
    class Meta:
        model = ClienteFisico
        fields = ('nome', 'cpf')