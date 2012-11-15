from django.conf.urls.defaults import patterns

from django_blog.models import Category


urlpatterns = patterns('',
    (r'^$',
        'django.views.generic.list_detail.object_list',
        {'queryset': Category.objects.all()},
        'blog_category_list'),
    (r'^(?P<slug>[-\w]+)/$',
        'django_blog.views.category_detail',
        '',
        'blog_category_detail'),)