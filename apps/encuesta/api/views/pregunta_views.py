from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.encuesta.models import *
from apps.encuesta.api.serializers import *

@api_view(['GET', 'POST'])
def pregunta_api_view(request,pk_encuesta=None):
    preguntas = Encuesta.objects.filter(id=pk_encuesta).first().preguntas
    if preguntas:
        if request.method == 'GET':
            preguntas = Encuesta.objects.filter(id=pk_encuesta).first().preguntas
            preguntas_serializer = PreguntasSerializer(preguntas, many=True)
            return Response(preguntas_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            pregunta_serializer = PreguntasSerializer(data=request.data)

            if pregunta_serializer.is_valid():
                pregunta_serializer.save()
                return Response({'message': 'pregunta creada correctamente!'}, status=status.HTTP_201_CREATED)

            return Response(pregunta_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'No se ha encontrado preguntas con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pregunta_detail_api_view(request, pk_encuesta=None,pk=None):

    encuesta = Encuesta.objects.filter(id=pk_encuesta).first()
    pregunta = encuesta.preguntas.filter(id=pk).first()

    if pregunta:
        if request.method == 'GET':
            pregunta_serializer = PreguntasSerializer(pregunta)
            return Response(pregunta_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            pregunta_serializer = PreguntasSerializer(pregunta, data=request.data)
            if pregunta_serializer.is_valid():
                pregunta_serializer.save()
                return Response(pregunta_serializer.data, status=status.HTTP_200_OK)
            return Response(pregunta_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            pregunta.delete()
            return Response({'message': 'pregunta Eliminada correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado preguntas con estos datos'}, status=status.HTTP_400_BAD_REQUEST)