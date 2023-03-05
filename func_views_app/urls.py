from django.urls import path,include
from .views import funkcija1,funkcija2,funkcija3

urlpatterns=[
    path("ime/",funkcija1),
    path("ploshtina-perimetar/",funkcija2),
    path("paren/",funkcija3)
]