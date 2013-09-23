# -*- coding: utf-8 -*-

# В этом файле мы регистрируем собственные модели в административном интерфейсе

from django.contrib import admin
from schedule_app.models import Teacher, Group, Student, Schedule 

class TeacherAdmin(admin.ModelAdmin):
	"""Настройка модели для админки"""

	# определяем какие поля отображать в админке
	list_display = ('first_name', 'partonymic', 'surname',)


class StudentInline(admin.TabularInline):
	"""Настройка модели для админки"""
	
	model = Student
	list_display = ('group', 'name',)


class GroupAdmin(admin.ModelAdmin):
	"""Настройка модели для админки"""

	list_display = ('group_code',)
	# вложенные модели
	inlines = [StudentInline,]


class ScheduleAdmin(admin.ModelAdmin):
	"""Настройка модели для админки"""

	list_display = ('day', 'time', 'group', 'teacher',)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Schedule, ScheduleAdmin)