# -*- coding: utf-8 -*-

from django.db import models


class Teacher(models.Model):
	"""Преподаватели языковых курсов"""
	
	first_name = models.CharField(max_length=50, verbose_name='Имя')
	partonymic = models.CharField(max_length=50, verbose_name='Отчество')
	surname = models.CharField(max_length=50, verbose_name='Фамилия')
	
	class Meta:
		verbose_name = 'Преподаватель'

	def __unicode__(self):
		return self.surname 


class Group(models.Model):
	"""Группы, изучающие языки"""
	
	group_code = models.CharField(max_length=7, verbose_name='Номер группы')

	class Meta:
		verbose_name = 'Группа'

	def __unicode__(self):
		return self.group_code


class Student(models.Model):
	"""Студенты, изучающие язык"""

	group = models.ForeignKey(Group, verbose_name='Группа')
	name = models.CharField(max_length=100, verbose_name='ФИО студента')

	class Meta:
		verbose_name = 'Студент'

	def __unicode__(self):
		return self.name


class Schedule(models.Model):
	"""Расписание занятий"""

	# Список дней недели.
	DAY_CHOICES = (
		('MO', 'Понедельник'),
		('TU', 'Вторник'),
		('WE', 'Среда'),
		('TH', 'Четверг'),
		('FR', 'Пятница'),
		('SA', 'Суббота'),
		('SU', 'Воскресенье'),
	)

	day = models.CharField(max_length=2, choices=DAY_CHOICES, verbose_name='День недели')
	time = models.TimeField(verbose_name='Время занятия')
	group = models.ForeignKey(Group, verbose_name='Группа')
	teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель')

	class Meta:
		verbose_name = 'Расписание'

	def __unicode__(self):
		return self.day