from django.urls import path

from appcoins.views import inicio, sobre, servicos, contato, privado


urlpatterns = [
    path('', inicio),
    path('sobre/', sobre),
    path('servicos/', servicos),
    path('contato/', contato),
    path('privado/', privado),
]