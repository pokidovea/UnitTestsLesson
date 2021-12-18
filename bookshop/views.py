from django.shortcuts import get_object_or_404, render

from bookshop.models import Book


def catalog(request):
    books = Book.objects.all()
    return render(request, 'catalog.html', {'books': books})


def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'book.html', {'book': book})
