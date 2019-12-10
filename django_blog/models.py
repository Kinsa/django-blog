from markdown import markdown

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __unicode__(self):
        if self.user.first_name and self.user.last_name:
            return "%s %s" % (self.user.first_name, self.user.last_name)
        else:
            return self.user.username

    def get_absolute_url(self):
        return reverse('blog:blog_author_detail', kwargs={'id': self.id})

    def live_entry_set(self):
        return self.entry_set.filter(status=Entry.LIVE_STATUS)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)

models.signals.post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)


class Category(models.Model):
    title = models.CharField(
        max_length=250,
        help_text='Maximum 250 characters.'
    )
    slug = models.SlugField(
        unique=True,
        help_text='Suggested value automatically generated from title. '
                  'Must be unique.'
    )

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_category_detail', kwargs={'slug': self.slug})

    def live_entry_set(self):
        from django_blog.models import Entry
        return self.entry_set.filter(status=Entry.LIVE_STATUS)


class LiveEntryManager(models.Manager):
    def get_queryset(self):
        return super(LiveEntryManager, self).get_queryset().filter(status=self.model.LIVE_STATUS)


class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(
        unique_for_date='pub_date',
        help_text='Suggested value automatically generated from title. '
                  'Must be unique.')
    body = models.TextField(
        help_text='Use Markdown to mark this up. '
                  'http://daringfireball.net/projects/markdown/syntax')
    body_html = models.TextField(editable=False, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        local_pub_date = timezone.localtime(self.pub_date)
        return reverse(
            'blog:blog_entry_detail', kwargs={
                'year': local_pub_date.strftime("%Y"),
                'month': local_pub_date.strftime("%b").lower(),
                'day': local_pub_date.strftime("%d"),
                'slug': self.slug
            }
        )

    def save(self, *args, **kwargs):
        if self.body:
            self.body_html = markdown(self.body)
        super(Entry, self).save(*args, **kwargs)

    objects = models.Manager()
    live = LiveEntryManager()
