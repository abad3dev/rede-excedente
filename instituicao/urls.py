
from os import path
from django.urls import path
from django.views.generic import TemplateView
from instituicao import views

urlpatterns = [
    path('cadastrar/', TemplateView.as_view(template_name='cadastrar_instituicao.html'), name='cadastrar_instituicao'),

]
