from .models import Person
from rest_framework import viewsets
from .serializers import PersonSerializer
from rest_framework.permissions import IsAuthenticated


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permissions_classes = (IsAuthenticated, )
