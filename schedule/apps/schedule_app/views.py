# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from models import Schedule, Group, Student, Teacher
import datetime

def schedule_page(request):
	"""Расписание занятий"""


	#определим даты текущей недели

	# текущая дата
	today = datetime.date.today()

	# вычисляем дату начала недели. 
	# определяем, каким днем недели по счету является текущий день и вычитаем это число из текущей даты. 
	start_week = today - datetime.timedelta(days=today.weekday())

	# к дате начала недели прибавляем 7 дней, чтобы вычислить дату конца недели
	end_week = start_week + datetime.timedelta(days = 7)

	schedule = Schedule.objects.select_related().all()

	schedule_mon = schedule.filter(day='MO')
	schedule_tue = schedule.filter(day='TU')
	schedule_wed = schedule.filter(day='WE')
	schedule_thu = schedule.filter(day='TH')
	schedule_fri = schedule.filter(day='FR')
	schedule_sat = schedule.filter(day='SA')
	schedule_sun = schedule.filter(day='SU')


	context = {
		'start_week': start_week,
		'end_week': end_week,
		'schedule_mon': schedule_mon,
		'schedule_tue': schedule_tue,
		'schedule_wed': schedule_wed,
		'schedule_thu': schedule_thu,
		'schedule_fri': schedule_fri,
		'schedule_sat': schedule_sat,
		'schedule_sun': schedule_sun,
	}
	
	return render(request, 'schedule_page.html', context)


def group_page(request, id):
	"""Список студентов выбранной группы"""

	try:
		group = Group.objects.get(id=id)
		students_list = Student.objects.filter(group__id=id)
	except Group.DoesNotExist:
		raise Http404
	
	context = {
		'students_list': students_list, 
		'name': request.GET.get('name', None)
	}

	return render(request, 'group_page.html', context)


def teacher_page(request, id):
	"""Информация о преподавателе"""

	teacher_info = get_object_or_404(Teacher, id=id)

	context = {
		'teacher_info': teacher_info,
	}

	return render(request, 'teacher_page.html', context)