
from os import path
from django.urls import path
from django.views.generic import TemplateView
from material import views

urlpatterns = [
       path('cadastrar/', views.cadastrar_material, name='cadastrar_material'),

]
