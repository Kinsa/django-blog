from django.conf.urls.defaults import patterns, url

from blog.feeds import LatestEntries


urlpatterns = patterns('',
    url(r'^(?P<url>.*)/$', LatestEntries(), '', 'blog_feed'),)
