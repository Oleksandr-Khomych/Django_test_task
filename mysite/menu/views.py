from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.template import loader

from .models import Menu, Language, Translate

# Create your views here.


def index(request):
    # Активна мова
    language = request.GET.get("lang", "eng")

    languages = Language.objects.all()
    root_menu_items = Menu.objects.filter(parent_element=None)
    submenu_items = Menu.objects.exclude(parent_element=None)
    translates = Translate.objects.filter(language=language)

    translates_dict = {}
    for item in translates:
        translates_dict[item.menu_id.menu_id] = item.text

    template = loader.get_template('menu/index.html')
    context = {
        'active_language': language,
        'languages': languages,
        'root_menu_items': root_menu_items,
        'submenu_items': submenu_items,
        'translates': translates,
    }
    return HttpResponse(template.render(context, request))
