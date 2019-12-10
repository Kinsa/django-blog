from django.contrib.syndication.views import Feed
from django.template.defaultfilters import striptags

from django_blog.models import Entry


class EntriesFeed(Feed):
    title = 'Blog'
    link = '/blog/'
    description = 'Latest blog posts'

    def items(self):
        return Entry.live.all()

    def item_pubdate(self, item):
        return item.pub_date

    def item_title(self, item):
        return striptags(item.title)

    def item_description(self, item):
        return item.body_html
