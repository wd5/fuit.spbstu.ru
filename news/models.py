# -*- coding: utf8 -*-
from django.db import models
import datetime
#import tinymce


class News(models.Model):
    title = models.CharField('Заголовок', max_length=300)
    date = models.DateField('Дата публикации', default=datetime.date.today)
#   short = models.CharField('Кратко', max_length = 300)
    text = models.TextField('Новость полностью')
    #img = models.ImageField(upload_to="news")
    show = models.BooleanField('Публиковать', default=True)

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

    def __unicode__(self):
        return str(self.date.strftime("%d.%m.%Y")) + ' - ' + self.title


class GlobalNews(News):
    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости и объявления'


class DeansNews(News):
    expired = models.DateField('Окончание публикации',
            default=datetime.date.today() + datetime.timedelta(weeks=4))

    class Meta:
        verbose_name = u'Объявление деканата'
        verbose_name_plural = u'Объявления деканата'


class ProfburoNews(News):
    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости профбюро'
