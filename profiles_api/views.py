from rest_framework.response import Response
from rest_framework.views import APIView

class ApiViewhello(APIView):
    """Test API view"""

    def get(self, request, format=None):
        
        return Response({'message':'Hello API'})

