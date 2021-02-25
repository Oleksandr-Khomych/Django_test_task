from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.template import loader

from .models import Menu

# Create your views here.


def index(request):
    info = HttpRequest.get_full_path(request)
    language = request.GET.get("lang", "en")
    print(f'\n\nlanguage = {language}\n\n')
    print(f'info = {info} !!!')
    root_menu_items = Menu.objects.filter(parent_element=None)
    submenu_items = Menu.objects.exclude(parent_element=None)
    template = loader.get_template('menu/index.html')
    context = {
        'root_menu_items': root_menu_items,
        'submenu_items': submenu_items
    }
    return HttpResponse(template.render(context, request))


# def index(request):
#     menu_item_list = Menu.objects.all()
#     context = {'menu_item_list': menu_item_list}
#     return render(request, 'menu/index.html', context)
