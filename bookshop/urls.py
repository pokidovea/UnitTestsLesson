from django.urls import path

from bookshop.views import book_details, catalog

urlpatterns = [
    path('', catalog, name='catalog'),
    path('details/<slug>', book_details, name='details')
]
