from django.urls import path

from bookshop.views import author_details, book_details, catalog

urlpatterns = [
    path('', catalog, name='catalog'),
    path('details/<slug>', book_details, name='details'),
    path('author/<id>', author_details, name='author_details'),
]
