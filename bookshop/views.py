from django.shortcuts import get_object_or_404, render

from bookshop.models import Author, Book


def catalog(request):
    books = Book.objects.all()
    return render(request, 'catalog.html', {'books': books})


def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'book.html', {'book': book})


def author_details(request, id):
    author = get_object_or_404(Author, id=id)

    return render(request, 'author.html', {'author': author})
