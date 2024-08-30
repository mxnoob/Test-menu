from django.contrib import admin

from .models import MenuItem


class MenuInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_name', 'parent', 'url', 'named_url')
    list_filter = ('menu_name',)
    inlines = [MenuInline]
