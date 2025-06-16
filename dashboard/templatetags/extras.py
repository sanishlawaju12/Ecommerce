from django import template

register = template.Library()

@register.filter
def pluck(qs, key):
    return [item.get(key) if isinstance(item, dict) else getattr(item, key, None) for item in qs]
