from django.shortcuts import render
from places.models import Place


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
                        "detailsUrl": ""
                    }
                }
            ]
            })
    context = {"geojson_data": geojson_data}

    return render(request, "index.html", context)
