from django.contrib import admin

from .models import (
    Matafuego, 
    TipoMatafuego,
    Cliente,
    Propiedad,
    Ticket,
    Configuracion,
    Certificado
)

admin.site.register(Matafuego)
admin.site.register(TipoMatafuego)
admin.site.register(Cliente)
admin.site.register(Propiedad)
admin.site.register(Ticket)
admin.site.register(Configuracion)
admin.site.register(Certificado)

