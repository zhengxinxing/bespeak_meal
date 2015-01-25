from django.shortcuts import render
from django.http import HttpResponse

from bespeak_meal.models import Week_menu, Person, Order

def index(request):
    person_list = Person.objects.all()
    menu = Week_menu.objects.get(pk=1) # 【待优化】由系统部署初始化来确保唯一实例
    b, l = (menu.breakfast_deadline, menu.lunch_deadline)
    week_menu = [ #【待优化】这个表达式怎么看都觉得丑陋
        (menu.menus[0].verbose_name, menu.mon),
        (menu.menus[1].verbose_name, menu.tue),
        (menu.menus[2].verbose_name, menu.wed),
        (menu.menus[3].verbose_name, menu.thu),
        (menu.menus[4].verbose_name, menu.fri),
        (menu.menus[5].verbose_name, menu.sat),
        (menu.menus[6].verbose_name, menu.sun),
    ]
    context = {'person_list': person_list,
        'week_menu': week_menu,
        'breakfast_deadline': b,
        'lunch_deadline': l,
    }
    return render(request, 'bespeak_meal/index.html', context)

def order(request):
    return HttpResponse('ordering')