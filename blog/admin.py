from django.contrib import admin
from blog.models import Category, Entry


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Category, CategoryAdmin)


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

    # customize the admin change list
    list_display = ('title', 'pub_date')

    # add a filter sidebar to the list view
    list_filter = ['pub_date', 'author', 'status']

    # add hierarchy navigation, by date, at the top of the list view
    # this allows us to drill down by year, then month, then day and so on
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)

admin.site.register(Entry, EntryAdmin)
