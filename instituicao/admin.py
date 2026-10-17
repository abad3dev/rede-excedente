from django.contrib import admin

# Register your models here.

from .models import Estado, Cidade, Instituicao

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Instituicao)

