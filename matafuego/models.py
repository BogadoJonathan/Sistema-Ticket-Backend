
from django.db import models
from multiselectfield import MultiSelectField


class Cliente(models.Model):
    razonSocial = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    celular = models.CharField(max_length=20,blank=True,null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['razonSocial']
    
    def __str__(self) -> str:
        return f'{self.razonSocial} - DNI: {self.dni}'

class Propiedad(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    TIPO_PROPIEDAD = (
        ('1','🚗'),
        ('2','🏠'),
    )
    typePropiedad = models.CharField(max_length=1, choices=TIPO_PROPIEDAD, help_text='Selecciona el tipo de propiedad')
    data = models.CharField(max_length=200)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
            return f'{self.TIPO_PROPIEDAD[int(self.typePropiedad)-1][1]} - {self.data}'

class TipoMatafuego(models.Model):
    class Capacidades(models.TextChoices):
        C1 = 1.0
        C2 = 2.0
        C2_5 = 2.5
        C3_5 = 3.5
        C5 = 5.0
        C6 = 6.0
        C7 = 7.0
        C8 = 8.0
        C10 = 10.0
        C12 = 12.0
        DEFAULT = 0
        
    title = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length = 200, blank=True)
    prioridad = models.BooleanField(default=False)
    ph = models.IntegerField(default=5)
    capacidades = MultiSelectField(choices=Capacidades.choices,
                                 max_choices=8,
                                 max_length=30,
                                 default=Capacidades.DEFAULT)
    class Meta:
        ordering = ['-prioridad','title']
    def __str__(self) -> str:
        return self.title
    
class Matafuego(models.Model):
    CAPACIDAD = (
        ('1',1.5),
        ('2',10.0),
        ('3',1.0),
    )
    tipo = models.ForeignKey(TipoMatafuego, on_delete=models.SET_NULL, null=True)
    idPropiedad = models.ForeignKey(Propiedad, on_delete=models.SET_NULL, null=True)
    procesado = models.BooleanField(default=False)
    capacidad = models.CharField(max_length=5,null=True)
    numeroMatafuego = models.CharField(max_length=20,blank=True,default='')
    anioFabricacion = models.CharField(max_length=4,default='',blank=True)
    mesPH = models.CharField(max_length=2,blank=True,default='') 
    anioPH = models.IntegerField(blank=True,null=True)
    mes = models.CharField(max_length=2,blank=True,default='') 
    year = models.CharField(max_length=2,blank=True,default='')
    idCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
        return f'{self.id}- {self.numeroMatafuego} - {self.tipo} {self.capacidad}'

class Certificado(models.Model):
    COLOR = (
        ('1','rosa'),
        ('2','verde'),
        ('3','azul'),
    )
    numero = models.CharField(max_length=50)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.SET_NULL, null=True)
    color =  models.CharField(max_length=1, choices=COLOR, help_text='Selecciona el color del certificado')
    matafuego = models.ForeignKey(Matafuego, on_delete=models.SET_NULL, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
        return self.numero

class Ticket(models.Model):
    number = models.IntegerField()
    clienteId = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    listMatafuegos = models.ManyToManyField(Matafuego)
    espera = models.BooleanField()
    finalizado = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['number']
    
    def __str__(self) -> str:
            return f'{self.number} | {self.clienteId} - finalizado: {self.finalizado}'

class Configuracion(models.Model):
    last_number_ticket = models.IntegerField(verbose_name='ultimo numero de ticket',null=True)
    last_serie_certificate_blue = models.CharField(verbose_name='🔵 serie certificado celetes', max_length=3,default='',null=True)
    last_number_certificate_blue = models.CharField(verbose_name='🔵 ultimo numero de certificado celeste',max_length=10,default=0,null=True)
    last_serie_certificate_pink = models.CharField(verbose_name='🔴 serie certificado rosa',max_length=3,default='',null=True)
    last_number_certificate_pink = models.CharField(verbose_name='🔴 ultimo numero de certificado rosa',max_length=10,default=0,null=True)
    last_serie_certificate_green = models.CharField(verbose_name='🟢 serie certificado verde',max_length=3,default='',null=True)
    last_number_certificate_green = models.CharField(verbose_name='🟢 ultimo numero de certificado verde',max_length=10,default=0,null=True)
    
    def __str__(self) -> str:
            return "configuracion inicial"

