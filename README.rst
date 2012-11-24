===========
Django Blog
===========

Installation from Source
========================

::

 $ git clone git://github.com/jbergantine/django-blog.git
 $ cd django-blog
 $ python setup.py install

You will also have to install `South <http://pypi.python.org/pypi/South/>`_ and `Markdown <http://pypi.python.org/pypi/Markdown/>`_.

Installation via PIP Requirements File
======================================

Include in the PIP requirements file the following lines:

::

 markdown==2.2.1
 south==0.7.6
 -e git://github.com/jbergantine/django-blog.git#egg=django_blog

And then install as normal (IE:)

::

 $ pip install -r path/to/requirements/file.txt


Setup the Project For the Application
=====================================

Add to the project's settings file tuple of INSTALLED_APPS: 

::

 'south',
 'django.contrib.markup',
 'django_blog',

In the project's urls.py file add: 

::

 url(r'^blog/author/', include('django_blog.urls.authors')),
 url(r'^blog/category/', include('django_blog.urls.categories')),
 url(r'^blog/feeds/', include('django_blog.urls.feeds')),
 url(r'^blog/', include('django_blog.urls.entries')),

Specify the AUTH_PROFILE_MODULE in the project's settings file: 

::

 AUTH_PROFILE_MODULE = 'django_blog.Author'

Migrate the database.

::

 $ ./manage.py migrate django_blog

A list of the latest 15 posts can now be linked to: 

::

 <a href="{% url blog_entry_archive %}">Blog</a>

A list of all posts in a specific year can be linked to, passing in the year: 

::

 <a href="{% url blog_entry_archive_year 2012 %}">2012</a>

A list of all posts in a specific month can be linked to, passing in year and month: 

::

 <a href="{% url blog_entry_archive_month 2012 01 %}">Jan, 2012</a>

A list of all posts on a specific day can be linked to, passing in year, month and day: 

::

 <a href="{% url blog_entry_archive_day 2012 01 01 %}">Jan 01, 2012</a>

A specific blog post can be linked to, passing in year, month, day and slug: 

::

 <a href="{% url blog_entry_detail 2012 01 01 'first-post' %}">First Post</a>
    
A list of all categories can be linked to: 

::

 <a href="{% url blog_category_list %}">Categories</a>

A list of all posts in a specific category can be linked to, passing in the slug of the category: 

::

 <a href="{% url blog_category_detail 'spying' %}">Posts about Spying</a>

A list of all the posts by a specific author can be linked to, passing in the id of the author: 

::

 <a href="{% url blog_author_detail 2 %}">Posts by James Bond</a>

The RSS feed can now be referred to in the ``<head>`` of your HTML templates: 

::
    
 <link rel="feed alternate" type="application/rss+xml" title="Blog" href="{% url blog_feed %}" />

Configure the Templates
=======================

By default the templates contain only the bare necessities. To override the default templates, create a directory called django_blog in your templates directory and copy the templates from the project into that directory in order to make adjustments to them. If you're using Virtualenv, ``cd`` to the root of the django project and execute the following command: ::

 cp -r $VIRTUAL_ENV/src/django-blog/django_blog/templates/django_blog templates/django_blog

Template Tags
=============

{% authors %}
*************

Returns an unordered list of all authors via the template ``_authors.html``.

Usage:

::

 {% load authors %}
 {% authors %}

{% categories %}
****************

Returns an unordered list of all categories via the template ``_categories.html``.

Usage:

::

 {% load categories %}
 {% categories %}