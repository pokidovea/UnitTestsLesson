# Generated by Django 4.0 on 2021-12-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count_in_storage',
            field=models.PositiveIntegerField(default=True),
        ),
    ]