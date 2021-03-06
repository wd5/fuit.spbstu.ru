import re
from django import template
from scientific.models import Conference, monthsTuple, ScienceWeekThesises
from django.db.models import Max, Min

register = template.Library()


@register.inclusion_tag('conference_pager.html', takes_context=True)
def get_pager_by_years(context):

    basepath = re.compile('[0-9]{4}/$').sub('', context['request'].path)
    years = [{'title': year, 'url': '%s%s/' % (basepath, year)} for year in
        range(
            Conference.objects.aggregate(Min('startDate'))['startDate__min'].year,
            Conference.objects.aggregate(Max('startDate'))['startDate__max'].year + 1
            )]
    return {'years': years, 'request': context['request']}


@register.inclusion_tag('month.html', takes_context=True)
def get_month(context, month):

    return {'month': monthsTuple[int(month) - 1][1]}


@register.inclusion_tag('files_list.html', takes_context=True)
def scienceWeekThesises(context):
    try:
        files = ScienceWeekThesises.objects.all()
    except:
        files = []
    return {
        'files': files,
        'request': context['request']
        }
