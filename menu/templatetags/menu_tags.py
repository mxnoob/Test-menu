from django import template
from django.template.context import RequestContext
from django.urls import resolve
from django.utils.safestring import mark_safe, SafeString

from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context: RequestContext, menu_name: str) -> SafeString:
    request = context['request']
    current_url = resolve(request.path_info).url_name
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related(
        'parent'
    )

    def build_menu_tree(parent=None):
        html = "<ul>"
        for item in menu_items:
            if item.parent != parent:
                continue

            url = item.get_absolute_url()
            is_active = url == request.path or item.named_url == current_url
            html += f"<li class='{is_active}'><a href='{url}'>{item.title}</a>"
            html += build_menu_tree(parent=item)
            html += "</li>"
        html += "</ul>"
        return mark_safe(html)

    return build_menu_tree()
