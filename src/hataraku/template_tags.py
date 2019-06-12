from django import template


register = template.Library()

@register.simple_tag
def go_uuid(request, **kwargs):
    updated = request.GET.copy()
    updated = kwargs
    return request.build_absolute_uri(updated.urlencode())