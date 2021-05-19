from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from teacher_app import serializers
from teacher_app import models
from teacher_app import permissions


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello messagewith our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})

        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST )


    def put(self, request, pk=None):
        """Handle the update of request"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle the partial update of the request"""

        return Response({"method":'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({"method":'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test api view sets"""
    serializer_class= serializers.HelloSerializer


    def list(self, request):
        """Return a hello message"""
        a_viewset= [
        'Uses action [list, creaet ,view , update, cdlete ]',
        'Automatically mas to IRLs using Routers',
        'Provers moe funcationluy ewith less code'
        ]

        return Response({"messgae": a_viewset})


    def create(self, request):
        """Create a new hello message"""
        serializer =self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response ({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({"message":"PUT"})

    def partial_update(self, request, pk=None):
        """Handle the partial updat"""
        return Response({"http_method":'PATCH'})

    def destroy(self, request, pk= None):
        """Handle deleting an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating an updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes =  (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends=(filters.SearchFilter,)
    search_fields= ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """HAndle creatin authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class StudentViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.StudentItemSerializer
    queryset = models.StudentItem.objects.all()
    permission_classes = {
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    }

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

class TeacherViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.TeacherItemSerializer
    queryset = models.TeacherItem.objects.all()
    permission_classes = {
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    }

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

class StaffViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.StaffItemSerializer
    queryset = models.StaffItem.objects.all()
    permission_classes = {
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    }




    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
