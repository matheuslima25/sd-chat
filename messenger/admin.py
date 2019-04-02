from django.contrib import admin

from .models import Menssagem

admin.site.site_header = "Administração | SD - Chat"
admin.site.site_title = "Administração | SD - Chat"


class MessagemAdmin(admin.ModelAdmin):
    list_display = ['autor', 'content', 'horario']
    readonly_fields = ('horario',)


admin.site.register(Menssagem, MessagemAdmin)
