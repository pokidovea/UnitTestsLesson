import datetime
from math import trunc

from django.db import models
from django.urls import reverse


class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=False)
    date_of_death = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100)
    portrait = models.ImageField(upload_to='portraits/', null=True, blank=True)
    bio = models.TextField(default='', blank=True)

    def __str__(self):
        if self.date_of_death:
            return f'{self.name} ({self.birthday}-{self.date_of_death})'
        return f'{self.name} ({self.birthday})'


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
    slug = models.SlugField(max_length=500, null=True)
    short_description = models.CharField(max_length=500, null=False, default='')
    page_count = models.PositiveIntegerField(null=False)
    language = models.CharField(max_length=3, choices=Language.choices)
    publisher = models.ForeignKey(Publisher, null=False, related_name='books', on_delete=models.CASCADE)
    publishing_year = models.SmallIntegerField(null=False)
    cover_type = models.CharField(max_length=10, choices=CoverType.choices)
    cost = models.PositiveIntegerField(null=False)
    picture = models.ImageField(upload_to='book_pictures/')
    count_in_storage = models.PositiveIntegerField(null=False, default=True)

    def __str__(self):
        return f'{self.title} ({self.publishing_year})'

    def get_authors(self):
        return self.authors.values_list('name', flat=True)

    def get_absolute_url(self):
        return reverse('details', args=[str(self.slug)])

    def cost_with_discount(self):
        today = datetime.date.today()

        # New Year discount 20%
        if today.month == 12 and (25 <= today.day <= 31):
            return trunc(self.cost * 0.8)

        # 8th March discount 10%
        if today.month == 3 and (5 <= today.day <= 12):
            return trunc(self.cost * 0.9)

        return self.cost
