from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import LeadModule
from .serializers import LeadSerializer
# Create your views here.

class CreateNewLeadViewSet(viewsets.ModelViewSet):

    queryset = LeadModule.objects.all()
    serializer_class = LeadSerializer
    permission_classes=[permissions.IsAuthenticated]

    def destroy(self, request, pk=None):

        instance = self.get_object()
        
        instance.delete()

        return Response({'message': 'Record Deleted Successfully. '}, status=HTTP_204_NO_CONTENT)