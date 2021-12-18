from django.shortcuts import render

from bookshop.models import Book


def catalog(request):
    books = Book.objects.all()
    return render(request, 'catalog.html', {'books': books})
