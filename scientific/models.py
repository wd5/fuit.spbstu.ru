# -*- coding: utf8 -*-

import datetime
from django.db import models
from staff.models import Persons as Persons, EducationDepartments

monthsTuple = (
        (1, u'Январь'),
        (2, u'Февраль'),
        (3, u'Март'),
        (4, u'Апрель'),
        (5, u'Май'),
        (6, u'Июнь'),
        (7, u'Июль'),
        (8, u'Август'),
        (9, u'Сентябрь'),
        (10, u'Октябрь'),
        (11, u'Ноябрь'),
        (12, u'Декабрь')
        )

conferenceTypes = (
        ('national', u'Всероссийская конференция'),
        ('local', u'Конференция СПбГПУ'),
        ('international', u'Международная конференция')
        )


class Conference(models.Model):
    title = models.CharField("Название конференции", max_length=512)
    conferenceType = models.CharField("Категория конференции",
            choices=conferenceTypes, max_length=32)
    startDate = models.DateField("Дата начала", blank=True)
    endDate = models.DateField("Дата окончания", blank=True)
    alternateDateMonth = models.IntegerField("Неточная дата", choices=monthsTuple,
            blank=True, null=True)
    alternateDateYear = models.IntegerField(blank=True)
    place = models.CharField("Место проведения", blank=True,
        help_text="Указывается только для всероссийских и международных конференций",
        max_length=32)
    organizers = models.TextField("Организатор")

    class Meta:
        verbose_name = u'Конференция'
        verbose_name_plural = u'Конференции'

    def __unicode__(self):
        return "%2s (%2s) - %2s" % (self.startDate, self.place, self.title)


class GrantAttachment(models.Model):
    title = models.CharField("Название файла", max_length=128)
    attachment = models.FileField("Файл", upload_to='files/grants/')
    description = models.CharField("Дополнительная информация", max_length=128, blank=True)

    class Meta:
        verbose_name = 'Приложение к гранту'
        verbose_name_plural = 'Приложения к гранту'

    def __unicode__(self):
        return self.title


class Grant(models.Model):
    title = models.CharField("Название конкурса (гранта)", max_length=255)
    text = models.TextField("Описание")
    year = models.DecimalField("Год",
        default=datetime.datetime.now().year,
        max_digits=4,
        decimal_places=0)
    attachments = models.ManyToManyField('GrantAttachment',
        verbose_name='Приложения',
        blank=True)

    class Meta:
        verbose_name = 'Конкурс (Грант)'
        verbose_name_plural = 'Конкурсы и гранты'

    def __unicode__(self):
        return u'%2s (%2d)' % (self.title, self.year)


class TeacherInterest(models.Model):
    teacher = models.ForeignKey(Persons, verbose_name='Преподаватель')
    department = models.ForeignKey(EducationDepartments, verbose_name='Кафедра')
    interests = models.TextField('Интересы преподавателя')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Научные интересы преподавателей'

    def __unicode__(self):
        return self.teacher.__unicode__()


class ScienceWeekThesises(models.Model):
    title = models.CharField('Название', max_length=64)
    attachment = models.FileField("Файл",
        upload_to='files/science_week_thesises/')

    class Meta:
        verbose_name = 'Тезисы недели науки'
        verbose_name_plural = 'Тезисы недели науки'

    def __unicode__(self):
        return self.title
