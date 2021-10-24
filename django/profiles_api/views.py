import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete',
            'Es similar a una vista tradicional de Django',
            'Node da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manualmente a los URLs'
        ]

        return Response({'message': 'Hello','an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request,pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request,pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request,pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset = [
            'Usa acciones (list, create, retrieve, update, partial_update',
            'Automaticamente mapea a los URLS usando RRouters',
            'Provee mas funcionalidad con menos codigo',
        ]

        return Response({'message': 'Hola!', 'a_viewset': a_viewset})

    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request,pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request,pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request,pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request,pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """"Creat y actualizar perfiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)