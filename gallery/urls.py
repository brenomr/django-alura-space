from django.urls import path
from .views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem') # name used to reference 'imagem' on url in the template
]
