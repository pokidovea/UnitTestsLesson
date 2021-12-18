from django.urls import path

from bookshop.views import catalog

urlpatterns = [
    path('', catalog, name='catalog'),
]
