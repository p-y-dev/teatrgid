def name_city_user(request):
    if not hasattr(request, "city_obj"):
        return {}

    return {'name_city_user': request.city_obj.name}
