from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from django_blog.models import Author, Category, Entry


class BlogCategoryTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_add_category(self):
        c = Category.objects.create(title='Test Category',
                                    slug='test-category')

        r = self.client.get(reverse('blog_category_list'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'blog/category_list.html')

        r = self.client.get(reverse('blog_category_detail',
            kwargs={'slug': c.slug}))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'blog/category_detail.html')

    def test_add_entry(self):
        user = User.objects.create_user('testuser',
                                        'testuser@domain.com',
                                        'testpassword')
        user.save()

        a = Author.objects.get(user__username='testuser')

        c = Category.objects.create(title='Test Category',
                                    slug='test-category')

        e = Entry.objects.create(title='Test Title',
                                 slug='test-title',
                                 body='Lorem ipsum...',
                                 author=a,
                                 category=c)

        r = self.client.get(reverse('blog_entry_archive'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'blog/entry_archive.html')

        r = self.client.get(reverse('blog_entry_archive_year',
            kwargs={'year': e.pub_date.strftime('%Y')}))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'blog/entry_archive_year.html')

        r = self.client.get(reverse('blog_entry_archive_month',
            kwargs={'year': e.pub_date.strftime('%Y'),
                    'month': e.pub_date.strftime('%b')}))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'blog/entry_archive_month.html')

        r = self.client.get(reverse('blog_entry_archive_day',
            kwargs={'year': e.pub_date.strftime('%Y'),
                    'month': e.pub_date.strftime('%b'),
                    'day': e.pub_date.strftime('%d')}))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'blog/entry_archive_day.html')

        r = self.client.get(reverse('blog_entry_detail',
            kwargs={'year': e.pub_date.strftime('%Y'),
                    'month': e.pub_date.strftime('%b'),
                    'day': e.pub_date.strftime('%d'),
                    'slug': e.slug}))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'blog/entry_detail.html')
