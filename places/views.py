from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.http import JsonResponse
from django.urls import reverse


def index(request):
    geojson_data = []
    places = Place.objects.all()
    for place in places:
        latitude = place.lat
        longitude = place.lng
        title = place.title
        geojson_data.append({
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [longitude, latitude]
                        },
                    "properties": {
                        "title": title,
                        "placeId": place.id,
                        "detailsUrl": reverse("show_place", args=[place.id])
                    }
                }
            ]
            })
    context = {"geojson_data": geojson_data}

    return render(request, "index.html", context)


def show_place(requests, place_id):
    place = get_object_or_404(Place, id=place_id)
    urls_image = []

    if place.images:
        for image in place.images.all():
            urls_image.append(image.images.url)
    else:
        urls_image.append("There is no photo for this location.")

    coordinates_place = {
        "lng": place.lng,
        "lat": place.lat
    }
    adress_place = {
        "title": place.title,
        "imgs": urls_image,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinstes": coordinates_place
    }
    return JsonResponse(adress_place)
