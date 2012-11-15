from django import template

from django_blog.models import Category


register = template.Library()


@register.inclusion_tag('blog/_categories.html')
def fetch_categories():
    categories = []
    try:
        all_categories = Category.objects.all()
        for c in all_categories:
            if len(c.live_entry_set()) > 0:
                categories.append(c)
    except:
        pass

    return {'categories': categories}
