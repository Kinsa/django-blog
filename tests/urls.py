from django.conf.urls import include, url


urlpatterns = [
    url(r'^blog/', include('django_blog.urls', namespace='blog')),
]
