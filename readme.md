## Installation

Add ``'blog',`` to the ``INSTALLED_APPS`` tuple in ``settings.py``.

Add ``'django.contrib.markup',`` to the ``INSTALLED_APPS`` tuple in ``settings.py``.

Add ``AUTH_PROFILE_MODULE = 'blog.Author'`` to ``settings.py``.

Add the following to the ``patterns()`` method in the project's primary ``urls.py`` file:

    url(r'^blog/author/', include('blog.urls.authors')),
    url(r'^blog/category/', include('blog.urls.categories')),
    url(r'^blog/feeds/', include('blog.urls.feeds')), 
    url(r'^blog/', include('blog.urls.entries')),

The RSS feed can now be referred to in the ``<head>`` of your HTML templates:
    
    <link rel="feed alternate" type="application/rss+xml" title="Blog" href="{% url blog_feed 'blog' %}" />