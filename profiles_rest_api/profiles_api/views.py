from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from profiles_api import serializers
from profiles_api import models, permissions
from rest_framework.authentication import TokenAuthentication


class HelloApiView(APIView):
    serializer_class = serializers.HelloSeriallizer
    def get(self, request, format =None):
        an_apiview = [
            'uses http methods',
            '2nd an _api view'
            '3rd an _api view'
            '4th an _api view'
        ]
    
        return Response({'message': 'hello! how you doin', 'an_apiview': an_apiview})


    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello mr {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk = None):
        return Response({'method': 'PUT'})


    def patch(self, request, pk = None):
        return Response({'method': 'patch'})
    
    
    def delete(self, request, pk = None):
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSeriallizer
    def list(self, request):    
        a_viewset =[
        
            'part one viewset',
        
            'part two viewset',
        
            'part three viewset',
        
        ]
        return Response({'message': 'Hello!', 'a_viewset':a_viewset})

    def create(elf, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello mr {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    
    def retrieve(self, request, pk = None):
        return Response({'method': 'get'})


    def update(self, request, pk = None):
        return Response({'method': 'put'})


    def partial_update(self, request, pk = None):
        return Response({'method': 'patch'})
    
    
    def destroy(self, request, pk = None):
        return Response({'method': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)