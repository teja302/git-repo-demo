from django import template
from blood_donate.models  import HomeNav_drop
register = template.Library()

@register.filter
def is_subdrop_active(admin_drop, request_path):
    return HomeNav_drop.objects.filter(nav_url=request_path, admin_drop=admin_drop).exists()