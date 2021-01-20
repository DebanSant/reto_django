from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.encuesta.models import *
from apps.encuesta.api.serializers import *

@api_view(['GET', 'POST'])
def categoria_api_view(request):

    if request.method == 'GET':
        # queryset
        categorias = CategoriaEncuesta.objects.all()
        categorias_serializer = CategoriaEncuestaSerializer(categorias, many=True)
        return Response(categorias_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        categoria_serializer = CategoriaEncuestaSerializer(data=request.data)

        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response({'message': 'categoria creada correctamente!'}, status=status.HTTP_201_CREATED)

        return Response(categoria_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detail_api_view(request, pk=None):

    categoria = CategoriaEncuesta.objects.filter(id=pk).first()

    if categoria:
        if request.method == 'GET':
            categoria_serializer = CategoriaEncuestaSerializer(categoria)
            return Response(categoria_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            categoria_serializer = CategoriaEncuestaSerializer(categoria, data=request.data)
            if categoria_serializer.is_valid():
                categoria_serializer.save()
                return Response(categoria_serializer.data, status=status.HTTP_200_OK)
            return Response(categoria_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            categoria.delete()
            return Response({'message': 'categoria Eliminada correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado categorias con estos datos'}, status=status.HTTP_400_BAD_REQUEST)