from places.models import Place
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404


def serialize_geojson(place):
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                    },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse("show_place", args=[place.id])
                    }
                }
            ]
        }


def index(request):
    places = Place.objects.prefetch_related('images')
    context = {"geojson_data": serialize_geojson(place) for place in places}

    return render(request, "index.html", context)


def show_place(requests, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        id=place_id
        )
    
    urls_image = []
    for image in place.images.all():
        urls_image.append(image.images.url) if place.images else None

    place_coordinates = {
        "lng": place.lng,
        "lat": place.lat
    }
    serialize_place = {
        "title": place.title,
        "imgs": urls_image,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinstes": place_coordinates
    }
    return JsonResponse(serialize_place)
