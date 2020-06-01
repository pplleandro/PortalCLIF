from django.contrib import admin

from ATI.models import ATI, Embalagem, Viagem, Pais, Porto, NCM, Notify, Representante, Importador, Comissaria, \
    Conteiner, Anexos, Faturador

admin.site.register(ATI)
admin.site.register(Embalagem)
admin.site.register(Viagem)
admin.site.register(Pais)
admin.site.register(Porto)
admin.site.register(NCM)
admin.site.register(Notify)
admin.site.register(Faturador)
admin.site.register(Representante)
admin.site.register(Importador)
admin.site.register(Comissaria)
admin.site.register(Conteiner)
admin.site.register(Anexos)
