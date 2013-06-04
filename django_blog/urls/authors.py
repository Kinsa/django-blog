from django.conf.urls import patterns


urlpatterns = patterns('',
    (r'^(?P<id>[-\d]+)/$',
        'django_blog.views.author_detail',
        '',
        'blog_author_detail'),)
