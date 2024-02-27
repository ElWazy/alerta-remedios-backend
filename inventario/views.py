from rest_framework import viewsets

from inventario import models, serializers


class RemedioViewSet(viewsets.ModelViewSet):
    queryset = models.Remedio.objects.all()
    serializer_class = serializers.RemedioSerializer
