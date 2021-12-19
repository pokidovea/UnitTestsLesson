from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from bookshop.logic import buy_a_book
from bookshop.models import Author, Book


@require_http_methods(['GET'])
def catalog(request):
    books = Book.objects.all()
    return render(request, 'catalog.html', {'books': books})


@require_http_methods(['GET'])
def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'book.html', {'book': book})


@require_http_methods(['GET'])
def author_details(request, id):
    author = get_object_or_404(Author, id=id)

    return render(request, 'author.html', {'author': author})


@csrf_exempt
@require_http_methods(['POST'])
def buy(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.count_in_storage == 0:
        result = False
        message = 'Out of stock'
    else:
        result = buy_a_book(book.id, book.cost_with_discount)

        if result:
            message = f'Book "{book}" purchased successfully'
        else:
            message = 'Processing service is unavailable. Please try later.'

    if result:
        book.count_in_storage -= 1
        book.save()

    return JsonResponse({'success': result, 'message': message})
