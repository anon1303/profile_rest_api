from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from profiles_api import serializers


class ApiViewhello(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        
        return Response({'message':'Hello API'})

    def post(self, request):
        """Create a hollo message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST                            
                            )
        
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message':'PUT'})
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'message':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'message':'DELETE'})