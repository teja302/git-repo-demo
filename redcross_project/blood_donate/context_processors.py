from .models import HomeNav_drop ,appfooter,appfooter1,appdown,gettouch,socialicon # Import your model

def dynamic_nav(request):
    # Retrieve the navigation items
    admin_drops=HomeNav_drop.objects.filter(parent_category=None)
    
    # You can perform any additional logic or filtering here if needed
    for admin_drop in admin_drops:
        admin_drop.is_active = admin_drop.is_active(request.path)

    # Return the navigation items in a dictionary
    return {'admin_drops': admin_drops}

def dynamic_footer(request):
    a = appfooter.objects.all()
    a1 = appfooter1.objects.all()
    a2 = appdown.objects.all()
    a3 = gettouch.objects.all()
    a4 = socialicon.objects.all()
    
    return {'footer_data': {'a': a, 'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4}}


from django.utils import timezone

def current_date(request):
    return {
        'today': timezone.now().date(),
    }