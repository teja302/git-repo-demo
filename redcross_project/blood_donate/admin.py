from django.contrib import admin
from .models import HomeNav_drop,appdown,appfooter,appfooter1,gettouch,socialicon ,blood , Announcement,tips_donation,contactus,content,Contactusadmin,contact
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html

class HomeNavDropAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'nav_name', 'nav_url', 'parent_category','order')
    actions = ['reorder_rows']
admin.site.register(HomeNav_drop, HomeNavDropAdmin)
admin.site.register(contact)
admin.site.register(appfooter1)
admin.site.register(appdown)
admin.site.register(appfooter)
admin.site.register(gettouch)
admin.site.register(content)
admin.site.register(contactus)

admin.site.register(Contactusadmin)

admin.site.register(tips_donation)

admin.site.register(socialicon)


class bloodCarouselAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'display_image','order')
    def display_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.photo.url)
    display_image.short_description = 'Image'
    actions = ['reorder_rows']
admin.site.register(blood , bloodCarouselAdmin)

admin.site.register(Announcement)