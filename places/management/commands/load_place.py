from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place

import requests 


class Command(BaseCommand):
    help = 'Добавляет места на карту через терминал'

    def handle(self, *args, **options):
        url = options['url']
        try:
            data_js = requests.get(url).json()
        except Exception as e:
            print(e)

        place, created = Place.objects.get_or_create(
            title=data_js.get('title'),
            description_long=data_js.get('description_long'),
            description_short=data_js.get('description_short'),
            lat=data_js['coordinates']['lat'],
            lng=data_js['coordinates']['lng'],
            )

        urls_image = data_js.get('imgs')
        if urls_image:
            for order, image_url in enumerate(urls_image, start=1):
                image = requests.get(image_url).content
                content = ContentFile(image, f'{order}.jpg')
                place.images.create(
                    images=content,
                    order=order,
                    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--url', dest='url', required=True,
            help='the url to process',
        )
