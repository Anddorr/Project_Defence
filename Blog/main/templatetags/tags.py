from django import template


register = template.Library()


@register.simple_tag
def edit_comment(list):
    list.pop(0)
    return ''