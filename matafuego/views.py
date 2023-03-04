from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Matafuego,
    TipoMatafuego,
    Cliente,
    Propiedad,
    Ticket,
    Configuracion,
    Certificado
    )
from .serializers import (
    MatafuegoSerializer,
    TipoMatafuegoSerializer,
    ClienteSerializer,
    PropiedadSerializer,
    TicketSerializer,
    ConfiguracionSerializer,
    CertificadoSerializer
)

class TipoMatafuegoModelViewSet(ModelViewSet):
    serializer_class = TipoMatafuegoSerializer
    queryset = TipoMatafuego.objects.all()
    http_method_names = ['get']

class MatafuegoModelViewSet(ModelViewSet):
    http_method_names = ['get','post','put']
    serializer_class = MatafuegoSerializer
    queryset = Matafuego.objects.all()

    def list(self,request):
        listado = request.query_params.get('listado',None)
        idCliente = request.query_params.get('idCliente',None)
        
        if listado:
            listado = listado.split(',')
            queryset = self.queryset.filter(pk__in=listado)
        elif idCliente:
            idCliente = int(idCliente)
            queryset = self.queryset.filter(idCliente=idCliente)
        else:
            queryset = Matafuego.objects.all()
        serializer = MatafuegoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
    def create(self, request):
        data = request.data 
        # year = str(data['year'])
        # # if len(year) >= 2:
        # #     data['year'] = int(year[-2:])
        # # else:
        # #     return Response("ingresa un año mayor a 2 digitos", status=status.HTTP_400_BAD_REQUEST)
        
        serializer = MatafuegoSerializer(data=data)
        if serializer.is_valid():
            print(serializer.errors)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ClientesModelViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    
    def list(self,request):
        query = request.query_params.get('query',None)
        if query:
            queryset = self.queryset.filter(Q(razonSocial__istartswith=query) | Q(dni__istartswith=query))
            # queryset = self.queryset.filter(razonSocial__dni__istartswith = query).values('razonSocial', 'dni')
        else:
            queryset = Cliente.objects.all()
        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class PropiedadModelViewSet(ModelViewSet):
    serializer_class = PropiedadSerializer
    queryset = Propiedad.objects.all()
    
    def list(self,request):
        idCliente = request.query_params.get('idCliente',None)
        patente = request.query_params.get('patente',None)
        queryset_ = Propiedad.objects.all()
        if idCliente:
            idCliente = int(idCliente)
            queryset_ = self.queryset.filter(idCliente=idCliente)
        if patente:
            queryset_ = self.queryset.filter(data=patente)
            
        serializer = PropiedadSerializer(queryset_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TicketModelViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    
    def list(self, request):
        number = request.query_params.get('number',None)
        
        queryset_ = self.queryset
        if number:
            number = int(number)
            queryset_ = self.queryset.filter(number=number)
        else:
            queryset_ = self.queryset.filter(finalizado=False)
        serializer = TicketSerializer(queryset_, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ConfiguracionModelViewSet(ModelViewSet):
    http_method_names = ['get','put']
    serializer_class = ConfiguracionSerializer
    queryset = Configuracion.objects.all()

class CertificadoModelViewSet(ModelViewSet):
    http_method_names = ['get','post']
    serializer_class = CertificadoSerializer
    queryset = Certificado.objects.all()
