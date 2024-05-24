from django.contrib import admin
from .models import UsuarioDb,CanchaDb, ReservaDb

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email']

admin.site.register(UsuarioDb, UsuarioAdmin)
admin.site.register(CanchaDb)
admin.site.register(ReservaDb)
