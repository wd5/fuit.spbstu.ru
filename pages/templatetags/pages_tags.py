# -*- coding: utf8 -*-

from django import template
from django.core.urlresolvers import resolve
from pages.models import Page
import re

monthsTupleV = (
            u'',
            u'января',
            u'февраля',
            u'марта',
            u'апреля',
            u'мая',
            u'июня',
            u'июля',
            u'августа',
            u'сентября',
            u'октября',
            u'ноября',
            u'декабря'
        )

register = template.Library()

@register.inclusion_tag('menu_items.html', takes_context=True)
def menu(context):
    return {
            'all': Page.objects.filter(show_in_menu = '1', 
                                       url__regex = '^/[^/]+/$'),
            'nested': Page.objects.filter(show_in_menu = '1',
                                          url__regex = '^/' + context['request'].path.split('/')[1] + '/[^/]+/$'),
                                          #url__regex = '^/about'  + '/[^/]+/$'),
            'request': context['request']
            }

@register.inclusion_tag('menu_full.html', takes_context = True)
def menuFull(context):
    raw_pages = Page.objects.filter(show_in_menu = '1',
                                url__regex = '^/([^/]+/){1,2}$')
    level1_re = re.compile('^/[^/]+/$')
    parent_re = re.compile('^/[^/]+/')
    pages = {}
    for page in raw_pages:
        if level1_re.match(page.url):
            pages[page.url] = {
                    'page': page,
                    'children': {}
                    }
        else:
            parent = parent_re.match(page.url).group()
            pages[parent]['children'][page.url] = page

    return {
            'pages': pages,
            'request': context['request']
            }

@register.inclusion_tag('breadcrumbs.html', takes_context=True)
def breadcrumbs(context, title=""):
    bc = context['request'].path.strip('/')
    bc = bc.split('/')
    path = '/'
    pages = []

    for i in bc:
        try:
            pages.append(Page.objects.get(url = path))
            path = path + i + '/'
        except :
            view, args, kwargs = resolve(path)
            pages.append({'url':path, 'title': view.title % kwargs})
            path = path + i + '/'
    try:
        pages.append(Page.objects.get(url = path))
    except :
        view, args, kwargs = resolve(context['request'].path)
        pages.append({'url':context['request'].path, 'title': view.title %
            kwargs})

    return {
            'pages': pages,
            'request': context['request']
            }

@register.inclusion_tag('date_interval.html', takes_context=True)
def date_interval(context, date_first, date_second):

    if date_first.year != date_second.year:
        result = u"%2s %2s %2s – %2s %2s %2s" % (date_first.day, 
            monthsTupleV[date_first.month], date_first.year, date_second.day,
            monthsTupleV[date_second.month], date_second.year)
    else:
        if date_first.month != date_second.month:
            result = u"%2s %2s – %2s %2s" % (date_first.day, 
            monthsTupleV[date_first.month], date_second.day,
            monthsTupleV[date_second.month])
        else:
            if date_first.day != date_second.day:
                result = u"%2s–%2s %2s" % (date_first.day, date_second.day,
                monthsTupleV[date_first.month])
            else:
                result = u"%2s %2s" % (date_first.day, monthsTupleV[date_first.month])

    return {'date': result}