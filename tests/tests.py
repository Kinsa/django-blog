from django.test import TestCase
from django.test.client import Client

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


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

        # TODO: test response returns up to 15 entries
        # TODO: test response only contains live entries

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

    def test_entry_detail_url(self):
        # Issue a GET request.
        response = self.client.get(
            reverse(
                'blog:blog_entry_detail',
                kwargs={
                    'year': '2012',
                    'month': 'jan',
                    'day': '01',
                    'slug': 'first-post'
                }
            )
        )

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/entry_detail.html')

    def test_category_list_url(self):
        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_category_list'))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/category_list.html')

    def test_category_detail_url(self):
        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_category_detail', kwargs={'slug': 'tradecraft'}))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/category_detail.html')

    def test_author_detail_url(self):
        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_author_detail', kwargs={'id': '1'}))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the correct template is being used.
        self.assertTemplateUsed(response, 'django_blog/author_detail.html')

    def test_feed_url(self):
        # Issue a GET request.
        response = self.client.get(reverse('blog:blog_feed'))

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # TODO: assert that it is an XML feed
        # TODO: assert that it only contains live entries
        # TODO: assert that it contains up to 30 entries
