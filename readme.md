## Installation

    $ pip install -r requirements.txt

## Usage

Add ``'blog',`` to the ``INSTALLED_APPS`` tuple in ``settings.py``.

Add ``'django.contrib.markup',`` to the ``INSTALLED_APPS`` tuple in ``settings.py``.

Add ``AUTH_PROFILE_MODULE = 'blog.Author'`` to ``settings.py``.

Migrate the database.

Add the following to the ``patterns()`` method in the project's primary ``urls.py`` file:

    url(r'^blog/author/', include('blog.urls.authors')),
    url(r'^blog/category/', include('blog.urls.categories')),
    url(r'^blog/feeds/', include('blog.urls.feeds')),
    url(r'^blog/', include('blog.urls.entries')),

A list of the latest 15 posts can now be linked to:

    <a href="{% url blog_entry_archive %}">Blog</a>

A list of all posts in a specific year can be linked to, passing in the year:

    <a href="{% url blog_entry_archive_year 2012 %}">2012</a>

A list of all posts in a specific month can be linked to, passing in year and month:

    <a href="{% url blog_entry_archive_month 2012 01 %}">Jan, 2012</a>

A list of all posts on a specific day can be linked to, passing in year, month and day:

    <a href="{% url blog_entry_archive_day 2012 01 01 %}">Jan 01, 2012</a>

A specific blog post can be linked to, passing in year, month, day and slug:

    <a href="{% url blog_entry_detail 2012 01 01 'first-post' %}">First Post</a>
    
A list of all categories can be linked to:

    <a href="{% url blog_category_list %}">Categories</a>

A list of all posts in a specific category can be linked to, passing in the slug of the category:

    <a href="{% url blog_category_detail 'spying' %}">Posts about Spying</a>

A list of all the posts by a specific author can be linked to, passing in the id of the author:

    <a href="{% url blog_author_detail 2 %}">Posts by James Bond</a>

The RSS feed can now be referred to in the ``<head>`` of your HTML templates:
    
    <link rel="feed alternate" type="application/rss+xml" title="Blog" href="{% url blog_feed %}" />

Edit the templates as necessary.

## Template Tags

### {% authors %}

Returns an unordered list of all authors via the template ``_authors.html``.

#### Usage

    {% load authors %}
    {% authors %}

### {% categories %}

Returns an unordered list of all categories via the template ``_categories.html``.

#### Usage

    {% load categories %}
    {% categories %}
