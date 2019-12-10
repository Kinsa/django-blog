from django.test import TestCase
from django.test.client import Client

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from django_blog.models import Entry


class ModelManagerTest(TestCase):
    fixtures = [
        'test_data_authors',
        'test_data_categories',
        'test_data_entries'
    ]

    def test_live_entry_set(self):
        live = Entry.objects.filter(status=Entry.LIVE_STATUS)
        hidden = Entry.objects.filter(status=Entry.HIDDEN_STATUS)
        draft = Entry.objects.filter(status=Entry.DRAFT_STATUS)

        # ensure there is appropriate test data to begin with
        self.assertTrue(live.count() > 0)
        self.assertTrue(hidden.count() > 0)
        self.assertTrue(draft.count() > 0)

        # Test that the hidden entries are not in the live set
        for entry in hidden:
            try:
                with self.subTest('Hidden entries are not in live set'):
                    self.assertFalse(entry.id in Entry.live.all().values_list('id', flat=True))
            except AttributeError:
                self.assertFalse(entry.id in Entry.live.all().values_list('id', flat=True))

        # Test that the draft entries are not in the live set
        for entry in draft:
            try:
                with self.subTest('Draft entries are not in live set'):
                    self.assertFalse(entry.id in Entry.live.all().values_list('id', flat=True))
            except AttributeError:
                self.assertFalse(entry.id in Entry.live.all().values_list('id', flat=True))

        # Test that the live entries are in the live set
        for entry in live:
            try:
                with self.subTest('Draft entries are not in live set'):
                    self.assertTrue(entry.id in Entry.live.values_list('id', flat=True))
            except AttributeError:
                self.assertTrue(entry.id in Entry.live.values_list('id', flat=True))


class RoutingTest(TestCase):
    fixtures = [
        'test_data_authors',
        'test_data_categories',
        'test_data_entries'
    ]

    def setUp(self):
        self.client = Client()

    def test_entry_archive_url(self):
        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_entry_archive'))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/entry_archive.html')

        # Check that the entry archive only contains live objects
        self.assertTrue(len(response.context['latest']), Entry.objects.filter(status=Entry.LIVE_STATUS).count())

    def test_entry_archive_year_url(self):
        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_entry_archive_year', kwargs={'year': '2012'}))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/entry_archive_year.html')

    def test_entry_archive_month_url(self):
        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_entry_archive_month', kwargs={'year': '2012', 'month': 'jan'}))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/entry_archive_month.html')

        # Check that the entry archive only contains live objects from the year and month
        self.assertTrue(
            len(response.context['object_list']),
            Entry.objects.filter(pub_date__year='2012', pub_date__month='01', status=Entry.LIVE_STATUS).count()
        )

    def test_entry_archive_day_url(self):
        # Issue a GET request.
        response = self.client.get(
            reverse(
                'blog:blog_entry_archive_day',
                kwargs={
                    'year': '2012',
                    'month': 'jan',
                    'day': '01'
                }
            )
        )

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/entry_archive_day.html')

        # Check that the entry archive only contains live objects from the year, month, and day
        self.assertTrue(
            len(response.context['object_list']),
            Entry.objects.filter(
                pub_date__year='2012',
                pub_date__month='01',
                pub_date__day='01',
                status=Entry.LIVE_STATUS
            ).count()
        )

    def test_entry_detail_url(self):
        entry = Entry.objects.filter(status=Entry.LIVE_STATUS).first()

        response = self.client.get(
            reverse(
                'blog:blog_entry_detail',
                kwargs={
                    'year': entry.pub_date.strftime('%Y'),
                    'month': entry.pub_date.strftime('%b').lower(),
                    'day': entry.pub_date.strftime('%d'),
                    'slug': entry.slug
                }
            )
        )

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/entry_detail.html')

    def test_entry_detail_url_draft_entry(self):
        entry = Entry.objects.filter(status=Entry.DRAFT_STATUS).first()

        # Issue a GET request.
        response = self.client.get(
            reverse(
                'blog:blog_entry_detail',
                kwargs={
                    'year': entry.pub_date.strftime('%Y'),
                    'month': entry.pub_date.strftime('%b').lower(),
                    'day': entry.pub_date.strftime('%d'),
                    'slug': entry.slug
                }
            )
        )

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/entry_detail.html')

    def test_entry_detail_url_hidden_entry(self):
        entry = Entry.objects.filter(status=Entry.HIDDEN_STATUS).first()

        # Issue a GET request.
        response = self.client.get(
            reverse(
                'blog:blog_entry_detail',
                kwargs={
                    'year': entry.pub_date.strftime('%Y'),
                    'month': entry.pub_date.strftime('%b').lower(),
                    'day': entry.pub_date.strftime('%d'),
                    'slug': entry.slug
                }
            )
        )

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 404)

    def test_category_list_url(self):
        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_category_list'))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/category_list.html')

    def test_category_detail_url(self):
        category = Entry.objects.all().first().category

        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_category_detail', kwargs={'slug': category.slug}))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/category_detail.html')

        # Check that the category detail only contains live objects from that category
        self.assertTrue(
            len(response.context['object_list']),
            Entry.objects.filter(category=category, status=Entry.LIVE_STATUS).count()
        )

    def test_author_detail_url(self):
        author = Entry.objects.all().first().author

        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_author_detail', kwargs={'id': author.pk}))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/author_detail.html')

        # Check that the author detail only contains live objects from that author
        self.assertTrue(
            len(response.context['object_list']),
            Entry.objects.filter(author=author, status=Entry.LIVE_STATUS).count()
        )

    def test_feed_url(self):
        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_feed'))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Chack that the response is XML
        self.assertEqual(response['Content-Type'], 'application/rss+xml; charset=utf-8')
