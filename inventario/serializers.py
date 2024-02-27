from rest_framework import serializers

from inventario import models


class RemedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Remedio
        fields = [
            "id",
            "nombre",
            "precio",
            "descripcion",
            "fecha_modificacion",
            "fecha_vencimiento",
        ]
