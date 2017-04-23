from .models import ListCity


def name_city_user(request):
    if not hasattr(request, "city_obj"):
        return {}

    return {'name_city_user': request.city_obj.name}


def list_city(request):
    return {
        'list_city': ListCity.objects.all().order_by("name")
    }
