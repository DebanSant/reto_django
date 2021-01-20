from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.encuesta.models import *
from apps.encuesta.api.serializers import *

@api_view(['GET', 'POST'])
def encuesta_api_view(request):

    if request.method == 'GET':
        # queryset
        encuestas = Encuesta.objects.all()
        encuestas_serializer = EncuestaSerializer(encuestas, many=True)
        return Response(encuestas_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        encuesta_serializer = EncuestaSerializer(data=request.data)

        if encuesta_serializer.is_valid():
            encuesta_serializer.save()
            return Response({'message': 'Encuesta creada correctamente!'}, status=status.HTTP_201_CREATED)

        return Response(encuesta_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def encuesta_detail_api_view(request, pk=None):

    encuesta = Encuesta.objects.filter(id=pk).first()

    if encuesta:
        if request.method == 'GET':
            encuesta_serializer = EncuestaSerializer(encuesta)
            return Response(encuesta_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            encuesta_serializer = EncuestaSerializer(encuesta, data=request.data)
            if encuesta_serializer.is_valid():
                encuesta_serializer.save()
                return Response(encuesta_serializer.data, status=status.HTTP_200_OK)
            return Response(encuesta_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            encuesta.delete()
            return Response({'message': 'Encuesta Eliminada correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado encuestas con estos datos'}, status=status.HTTP_400_BAD_REQUEST)