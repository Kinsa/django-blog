from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

from django_blog.models import Author, Category


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(
        request,
        'django_blog/category_detail.html',
        {'object_list': category.live_entry_set(), 'category': category},
    )


def author_detail(request, id):
    author = get_object_or_404(Author, pk=id)
    return render(
        request,
        'django_blog/author_detail.html',
        {'object_list': author.live_entry_set(), 'author': author},
    )
