import markdown
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags

register = template.Library()

# HTML変換用
@register.filter
def markdown_to_html(text):
    return mark_safe(markdown.markdown(text))

# プレーンテキスト変換用
@register.filter
def markdown_to_plain(text):
    html = markdown.markdown(text)
    return strip_tags(html)