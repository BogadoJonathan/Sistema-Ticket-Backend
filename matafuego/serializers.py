
from rest_framework import serializers

from .models import (
    Matafuego,
    TipoMatafuego,
    Cliente,
    Propiedad,
    Ticket,
    Configuracion,
    Certificado
)

class MatafuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matafuego
        fields = "__all__"

class TipoMatafuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMatafuego
        fields = "__all__"

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = "__all__"

class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = "__all__"