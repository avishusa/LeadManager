from leads.models import Lead
from rest_framework import viewsets,permissions
from .serialisers import LeadSerializers

class LeadviewSet(viewsets.ModelViewSet):
    queryset=Lead.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=LeadSerializers