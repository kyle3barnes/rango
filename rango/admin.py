from django.contrib import admin
from rango.models import Category, Page

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Statistics', {'fields': ['views', 'likes']}),
    ]


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    fieldsets = [
        (None, {'fields': ['title', 'url']}),
        ('Category', {'fields': ['category']}),
        ('Statistics', {'fields': ['views']}),
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
