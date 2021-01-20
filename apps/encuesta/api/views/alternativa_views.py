from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.encuesta.models import *
from apps.encuesta.api.serializers import *

@api_view(['GET', 'POST'])
def alternativa_api_view(request,pk_encuesta=None,pk_pregunta=None):

    alternativas = Encuesta.objects.filter(id=pk_encuesta).first().preguntas.filter(id=pk_pregunta).first().alternativas
    if alternativas:
        if request.method == 'GET':
            alternativas = Encuesta.objects.filter(id=pk_encuesta).first().preguntas.filter(id=pk_pregunta).first().alternativas
            alternativa_serializer = AlternativasSerializer(alternativas, many=True)
            return Response(alternativa_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            alternativa_serializer = AlternativasSerializer(data=request.data)

            if alternativa_serializer.is_valid():
                alternativa_serializer.save()
                return Response({'message': 'alternativa creada correctamente!'}, status=status.HTTP_201_CREATED)

            return Response(alternativa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'No se ha encontrado preguntas con estos datos'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def alternativa_detail_api_view(request,pk_encuesta=None,pk_pregunta=None,pk_alternativa=None):

    alternativa = Encuesta.objects.filter(id=pk_encuesta).first().preguntas.filter(id=pk_pregunta).first().alternativas.filter(id=pk_alternativa).first()

    if alternativa:
        if request.method == 'GET':
            alternativa_serializer = AlternativasSerializer(alternativa)
            return Response(alternativa_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            alternativa_serializer = AlternativasSerializer(alternativa, data=request.data)
            if alternativa_serializer.is_valid():
                alternativa_serializer.save()
                return Response(alternativa_serializer.data, status=status.HTTP_200_OK)
            return Response(alternativa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            alternativa.delete()
            return Response({'message': 'alternativa Eliminada correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado alternativa con estos datos'}, status=status.HTTP_400_BAD_REQUEST)