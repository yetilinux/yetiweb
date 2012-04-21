from datetime import datetime, timedelta
from pytz import utc

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from main.models import Package
from news.models import News
from packages.utils import get_group_info, get_split_packages_info

class PackagesSitemap(Sitemap):
    changefreq = "weekly"
    priority = "0.5"

    def items(self):
        return Package.objects.all().order_by()

    def lastmod(self, obj):
        return obj.last_update


class PackageFilesSitemap(PackagesSitemap):
    changefreq = "weekly"
    priority = "0.2"

    def location(self, obj):
        return PackagesSitemap.location(self, obj) + 'files/'

    def lastmod(self, obj):
        return obj.files_last_update


class PackageGroupsSitemap(Sitemap):
    changefreq = "weekly"
    priority = "0.4"

    def items(self):
        return get_group_info()

    def lastmod(self, obj):
        return obj['last_update']

    def location(self, obj):
        return '/groups/%s/%s/' % (obj['arch'], obj['name'])


class SplitPackagesSitemap(Sitemap):
    changefreq = "weekly"
    priority = "0.3"

    def items(self):
        return get_split_packages_info()

    def lastmod(self, obj):
        return obj['last_update']

    def location(self, obj):
        return '/packages/%s/%s/%s/' % (
                obj['repo'].name.lower(), obj['arch'], obj['pkgbase'])


class NewsSitemap(Sitemap):
    priority = "0.8"

    def __init__(self):
        now = datetime.utcnow().replace(tzinfo=utc)
        self.one_day_ago = now - timedelta(days=1)
        self.one_week_ago = now - timedelta(days=7)

    def items(self):
        return News.objects.all().order_by()

    def lastmod(self, obj):
        return obj.last_modified

    def changefreq(self, obj):
        if obj.last_modified > self.one_day_ago:
            return 'daily'
        if obj.last_modified > self.one_week_ago:
            return 'weekly'
        return 'yearly'


class BaseSitemap(Sitemap):
    base_viewnames = (
            ('index', 1.0, 'hourly'),
            ('packages-search', 0.8, 'hourly'),
            ('page-keys', 0.8, 'weekly'),
            ('news-list', 0.7, 'weekly'),
            ('groups-list', 0.5, 'weekly'),
            ('mirror-status', 0.4, 'hourly'),
            'page-about',
            'page-art',
            'page-svn',
            'page-devs',
            'page-tus',
            'page-fellows',
            'page-donate',
            'page-download',
            'feeds-list',
            'mirror-list',
            'mirrorlist',
            'packages-differences',
            'releng-test-overview',
            'visualize-index',
    )

    def items(self):
        return self.base_viewnames

    def location(self, obj):
        name = obj
        if isinstance(obj, tuple):
            name = obj[0]
        return reverse(name)

    def priority(self, obj):
        if isinstance(obj, tuple):
            return obj[1]
        return 0.7

    def changefreq(self, obj):
        if isinstance(obj, tuple):
            return obj[2]
        return 'monthly'

# vim: set ts=4 sw=4 et:
