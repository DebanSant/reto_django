from rest_framework import serializers
from apps.encuesta.models import *

class CategoriaEncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaEncuesta
        fields = '__all__'

class AlternativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativas
        fields = '__all__'

class PreguntasSerializer(serializers.ModelSerializer):
    alternativas = AlternativasSerializer(read_only=True,many=True)
    class Meta:
        model = Preguntas
        fields = '__all__'


class EncuestaSerializer(serializers.ModelSerializer):
    categories = CategoriaEncuestaSerializer(read_only=True,many=True)
    preguntas = PreguntasSerializer(read_only=True,many=True)
    class Meta:
        model = Encuesta
        fields = '__all__'



