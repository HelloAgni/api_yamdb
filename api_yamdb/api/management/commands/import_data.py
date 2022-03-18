# FIXME: перенести каталог management на уровень выше, в проект
from django.core.management.base import BaseCommand
import csv
from django.conf import settings

from reviews.models import Genre, Category
# from reviews.models import User, Comment, Title, Review

Models = {
    # User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    # Comment: 'comments.csv',
    # Title: 'titles.csv',
    # Review: 'review.csv',
}


class Command(BaseCommand):
    help = 'Загрузка данных из csv файлов'

    def handle(self, *args, **options):
        for model, csv_files in Models.items():
            with open(
                # FIXME: использовать STATICFILES_DIRS
                # FIXME: получить переменную через getattr(settings...)
                f'{settings.BASE_DIR}/static/data/{csv_files}',
                'r',
                encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                # TODO: очищать базу перед добавлением
                # TODO: делать запрос пользователю на очистку
                model.objects.bulk_create(
                    model(**data) for data in reader
                )
            self.stdout.write(
                f'Данные {model.__name__} успешно загружены в БД')
