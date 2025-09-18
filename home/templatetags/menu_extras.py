from django import template

register = template.Library()

@register.filter
def availability_status(menu_item):
    """
    Returns 'Coming Soon' if the menu item is unavailable,
    otherwise returns its price.
    """
    if not menu_item.available:
        return "Coming Soon"
    return f"${menu_item.price}"
