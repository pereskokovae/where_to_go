from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image

import requests
import time

ERROR_SLEEP_TIME = 60


class Command(BaseCommand):
    help = 'Добавляет места на карту через терминал'

    def handle(self, *args, **options):
        url = options['url']
        try:
            payload = requests.get(url).json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error occurred: {e}")
            time.sleep(ERROR_SLEEP_TIME)
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            time.sleep(ERROR_SLEEP_TIME)

        place, created = Place.objects.get_or_create(
            title=payload.get('title'),
            defaults={
                'long_description': payload.get('description_long'),
                'short_description': payload.get('description_short'),
                'lat': payload['coordinates']['lat'],
                'lng': payload['coordinates']['lng'],
            }
        )

        urls_image = payload.get('imgs')
        if urls_image:
            try:
                for order, image_url in enumerate(urls_image, start=1):
                    image = requests.get(image_url).content
                    content = ContentFile(image, f'{order}.jpg')

                    image_object, created = Image.objects.get_or_create(
                        place=place,
                        )
                    if created:
                        image_object.images.save(
                            f'{order}.jpg',
                            content,
                            save=True
                            )
            except requests.exceptions.HTTPError as e:
                print(f"HTTP Error occurred: {e}")
                time.sleep(ERROR_SLEEP_TIME)
            except requests.exceptions.ConnectionError as e:
                print(f"Connection Error: {e}")
                time.sleep(ERROR_SLEEP_TIME)

    def add_arguments(self, parser):
        parser.add_argument(
            '--url', dest='url', required=True,
            help='the url to process',
        )
