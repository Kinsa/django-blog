from django.conf.urls.defaults import patterns, url

from django_blog.models import Entry
from django.views.generic.dates import ArchiveIndexView


entry_info_dict = {
    'queryset': Entry.live.all(),
    'date_field': 'pub_date',
}

entry_detail_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    url(r'^$', ArchiveIndexView.as_view(queryset=Entry.live.all(),
        date_field='pub_date'), name='blog_entry_archive'),
    (r'^(?P<year>\d{4})/$',
        'archive_year',
        dict(entry_info_dict, make_object_list=True),
        'blog_entry_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        'archive_month',
        entry_info_dict,
        'blog_entry_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
        'archive_day',
        entry_info_dict,
        'blog_entry_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        'object_detail',
        entry_detail_dict,
        'blog_entry_detail'),)
