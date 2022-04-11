from django.shortcuts import render
from geopy.distance import distance
from main.models import Restaurant, Menu


def main_index(request):
    long = request.GET.get('long', 69.203732)
    lat = request.GET.get('lat',41.352657)
    current_point = (float(lat), float(long))

    result = []
    for row in Restaurant.objects.order_by('-id').all():
        restaurant_point = (row.lat, row.long)

        row.distance = distance(restaurant_point, current_point).meters
        result.append(row)

    result.sort(key=lambda r: r.distance)

    return render(request, 'main/index.html', {
      'restaurants': result
    })

def main_menu(request,rid):
    restaurant = Restaurant.objects.get(id=rid)

    return render(request, 'main/menu.html', {
        'restaurant':restaurant,
        'menu': Menu.objects.filter(restaurant_id=rid).order_by('id').all()
    })