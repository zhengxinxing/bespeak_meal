from django.contrib import admin
from django.db import models
from django import forms

from bespeak_meal.models import Person, Person_category, Week_menu


class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'remarks')
	fieldsets = [
		(None, 			{'fields': ['name']}),
		('按哪种收费方式', 	{'fields': ['category']}),
		('备注', 			{'fields': ['remarks']}),
	]

class PersonInline(admin.TabularInline):
	model = Person

class Person_categoryAdmin(admin.ModelAdmin):
	def count_persons(obj, obj2):
		return Person.objects.all().count()
	count_persons.short_description = '所属人员数量'

	list_display = ('name', 'breakfast_charge', 'lunch_charge',
		'dinner_charge', 'remarks', 'count_persons')

	# 让管理员在 人员分类 的界面下，可以直接增减属于该类的人员
	inlines = [PersonInline,]

class Week_menuAdmin(admin.ModelAdmin):
	formfield_overrides = {
		# 调整文本窗口大小，后期建议改到 views 里面去
        models.TextField: {
        	'widget': forms.Textarea(
        		attrs={	'rows': 3, 'cols': 64, } )
        },
    }

admin.site.register(Person, PersonAdmin)
admin.site.register(Person_category, Person_categoryAdmin)
admin.site.register(Week_menu, Week_menuAdmin)