from django.shortcuts import render


def index(request):
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.62, 55.793676]
                    },
                "properties": {
                    "title": "Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": "./places/moscow_legends.json"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.64, 55.753676]
                    },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": "./places/roofs24.json"
                }
            }
        ]
    }
    context = {"geojson_data": geojson_data}

    return render(request, "index.html", context)
