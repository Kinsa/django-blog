from django.conf.urls import url
from django.views.generic.list import ListView
from django.views.generic.dates import (
    ArchiveIndexView,
    DateDetailView,
    DayArchiveView,
    MonthArchiveView,
    YearArchiveView
)

from django_blog.feeds import EntriesFeed
from django_blog.models import Category, Entry
from django_blog.views import author_detail, category_detail

app_name = 'blog'


urlpatterns = [
    url(
        r'^$',
        ArchiveIndexView.as_view(
            date_field='pub_date',
            queryset=Entry.live.all()
        ),
        name='blog_entry_archive'
    ),

    url(
        r'^author/(?P<id>[\d]+)/$',
        author_detail,
        name='blog_author_detail'
    ),

    url(
        r'^category/$',
        ListView.as_view(queryset=Category.objects.all()),
        name='blog_category_list'
    ),
    url(
        r'^category/(?P<slug>[-\w]+)/$',
        category_detail,
        name='blog_category_detail'
    ),

    url(r'^feed/$', EntriesFeed(), name='blog_feed'),

    url(
        r'^(?P<year>\d{4})/$',
        YearArchiveView.as_view(
            date_field='pub_date',
            make_object_list=True,
            queryset=Entry.live.all()
        ),
        name='blog_entry_archive_year'
    ),

    url(
        r'^(?P<year>\d{4})/(?P<month>[-\w]+)/$',
        MonthArchiveView.as_view(
            date_field='pub_date',
            queryset=Entry.live.all()
        ),
        name='blog_entry_archive_month'
    ),

    url(
        r'^(?P<year>\d{4})/(?P<month>[-\w]+)/(?P<day>\d{2})/$',
        DayArchiveView.as_view(
            date_field='pub_date',
            queryset=Entry.live.all()
        ),
        name='blog_entry_archive_day'
    ),

    url(
        r'^(?P<year>\d{4})/(?P<month>[-\w]+)/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(
            date_field='pub_date',
            queryset=Entry.objects.exclude(status=Entry.HIDDEN_STATUS),
        ),
        name='blog_entry_detail'
    ),
]
