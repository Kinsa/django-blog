from django.conf.urls.defaults import patterns, url

from django_blog.feeds import LatestEntries


urlpatterns = patterns('',
    url(r'^$', LatestEntries(), '', 'blog_feed'),)
