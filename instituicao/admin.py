from django.contrib import admin

from material.models import Material, TipoMaterial

# Register your models here.

from .models import Estado, Cidade, Instituicao

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Instituicao)
admin.site.register(Material)
admin.site.register(TipoMaterial)
