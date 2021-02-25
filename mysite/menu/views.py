from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Menu

# Create your views here.


def index(request):
    root_menu_items = Menu.objects.filter(parent_element=None)
    print(f'root_menu_items = {root_menu_items}')
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
