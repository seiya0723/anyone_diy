from django import template
register = template.Library()

@register.simple_tag()
def url_replace(request, key, value):
    copied      = request.GET.copy()
    copied[key] = value
    return copied.urlencode()



## 管理サイトに表示させる会員数及びプロジェクト数を計算する

"""
from users.models import CustomUser

@register.simple_tag()
def total_members():
    return CustomUser.objects.filter(is_active=True,is_staff=False).count()
"""
