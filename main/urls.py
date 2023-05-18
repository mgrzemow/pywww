from django.urls import path
from main.views import hello_world, kontakty

urlpatterns = [
    path('kontakty/', kontakty),
    path('', hello_world),
]
