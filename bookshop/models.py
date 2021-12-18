from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=200)


class Author(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=False)
    date_of_death = models.DateField(null=True)
    country = models.CharField(max_length=100)
    portrait = models.ImageField(upload_to='portraits/')
    bio = models.TextField(default='')


class Book(models.Model):
    class Language(models.TextChoices):
        ENGLISH = 'en'
        RUSSIAN = 'ru'
        GERMAN = 'de'
        FRENCH = 'fr'

    class CoverType(models.TextChoices):
        SOFT = 'soft'
        HARD = 'hard'

    authors = models.ManyToManyField(Author, related_name='books')
    title = models.CharField(max_length=500, null=False)
    short_description = models.CharField(max_length=500, null=False, default='')
    page_count = models.PositiveIntegerField(null=False)
    language = models.CharField(max_length=3, choices=Language.choices)
    publisher = models.ForeignKey(Publisher, null=False, related_name='books', on_delete=models.CASCADE)
    publishing_year = models.SmallIntegerField(null=False)
    cover_type = models.CharField(max_length=10, choices=CoverType.choices)
    cost = models.PositiveIntegerField(null=False)
    picture = models.ImageField(upload_to='book_pictures/')
