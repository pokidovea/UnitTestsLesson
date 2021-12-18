from django.contrib import admin

from bookshop.models import Author, Book, Publisher


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthday', 'date_of_death', 'country']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title', 'publishing_year']}
    list_display = ['title', 'publishing_year', 'language', 'cover_type', 'publisher']
    list_filter = ['authors__name', 'publishing_year']
    filter_horizontal = ['authors']
