from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image

import requests
import time
import logging

ERROR_SLEEP_TIME = 60


class Command(BaseCommand):
    help = 'Добавляет места на карту через терминал'

    def handle(self, *args, **options):
        url = options['url']
        try:
            response = requests.get(url)
            response.raise_for_status()
            payload = response.json()

            place, created = Place.objects.get_or_create(
                title=payload.get('title'),
                defaults={
                    'long_description': payload.get('description_long'),
                    'short_description': payload.get('description_short'),
                    'lat': payload['coordinates']['lat'],
                    'lng': payload['coordinates']['lng'],
                }
            )

            urls_image = payload.get('imgs', [])
            if payload.get('imgs'):
                for order, image_url in enumerate(urls_image, start=1):
                    try:
                        image = requests.get(image_url).content
                        content = ContentFile(image, f'{order}.jpg')

                        image_object, created = Image.objects.get_or_create(
                            place=place,
                            image=content,
                            order=order
                            )
                        if not created:
                            print(f"The image {image_object} has already been added")

                    except requests.exceptions.RequestException as e:
                        logging.error(f'Error loading image {image_url}: {e}')
                        time.sleep(ERROR_SLEEP_TIME)

        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP Error occurred: {e}")
            time.sleep(ERROR_SLEEP_TIME)
        except requests.exceptions.ConnectionError as e:
            logging.error(f"Connection Error: {e}")
            time.sleep(ERROR_SLEEP_TIME)

    def add_arguments(self, parser):
        parser.add_argument(
            '--url', dest='url', required=True,
            help='the url to process',
        )
