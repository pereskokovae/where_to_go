from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place

import requests
import time


class Command(BaseCommand):
    help = 'Добавляет места на карту через терминал'

    def handle(self, *args, **options):
        url = options['url']
        try:
            raw_js = requests.get(url).json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error occurred: {e}")
            time.sleep(60)
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            time.sleep(60)

        place, created = Place.objects.get_or_create(
            title=raw_js.get('title'))
   
        if created:
            Place.objects.update_or_create(
                long_description=raw_js.get('description_long'),
                short_description=raw_js.get('description_short'),
                lat=raw_js['coordinates']['lat'],
                lng=raw_js['coordinates']['lng'],
                )

        urls_image = raw_js.get('imgs')
        if urls_image:
            try:
                for order, image_url in enumerate(urls_image, start=1):
                    image = requests.get(image_url).content
                    content = ContentFile(image, f'{order}.jpg')
                    place.images.create(
                        images=content,
                        order=order,
                        )
            except requests.exceptions.HTTPError as e:
                print(f"HTTP Error occurred: {e}")
                time.sleep(60)
            except requests.exceptions.ConnectionError as e:
                print(f"Connection Error: {e}")
                time.sleep(60)
      
    def add_arguments(self, parser):
        parser.add_argument(
            '--url', dest='url', required=True,
            help='the url to process',
        )
