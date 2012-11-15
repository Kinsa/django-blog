from django.conf.urls.defaults import patterns


urlpatterns = patterns('',
    (r'^(?P<id>[-\d]+)/$',
        'blog.views.author_detail',
        '',
        'blog_author_detail'),)
