from places.models import Place
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404


def get_features(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [float(place.lng), float(place.lat)]
            },
        "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse("show_place", args=[place.id])
        }
    }


def serialized_geojson():
    places = Place.objects.prefetch_related('images')
    geojson = {
        "type": "FeatureCollection",
        "features": [get_features(place) for place in places]
    }
    return geojson


def index(request):
    context = {'geojson_data': serialized_geojson()}
    return render(request, "index.html", context)


def show_place(requests, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        id=place_id
        )

    urls_image = [
        image.images.url for image in place.images.all()
        ] if place.images else None

    place_coordinates = {
        "lng": place.lng,
        "lat": place.lat
    }
    serialized_place = {
        "title": place.title,
        "imgs": urls_image,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinstes": place_coordinates
    }
    return JsonResponse(serialized_place)
