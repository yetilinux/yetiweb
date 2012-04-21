from django.http import Http404
from django.views.decorators.cache import cache_page
from django.views.generic.simple import direct_to_template


RETRO_YEAR_MAP = {
    2002: 'index-20020328.html',
    2003: 'index-20030330.html',
    2004: 'index-20040327.html',
    2005: 'index-20050328.html',
    2006: 'index-20060328.html',
    2007: 'index-20070324.html',
    2008: 'index-20080311.html',
    2009: 'index-20090327.html',
    2010: 'index-20100208.html',
    2011: 'index-20110212.html',
}


@cache_page(1800)
def retro_homepage(request, year):
    year = int(year)
    template = RETRO_YEAR_MAP.get(year, None)
    if template is None:
        raise Http404
    context = {
        'year': year,
    }
    return direct_to_template(request, 'retro/%s' % template, context)

# vim: set ts=4 sw=4 et:
