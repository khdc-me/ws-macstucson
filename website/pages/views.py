from django.shortcuts import render

from datetime import datetime


# Views
def home(request):
    pg_name = 'home'
    is_open = check_is_open()
    return render(request, 'home.html', {
                                            'is_open': is_open,
                                            'pg_name': pg_name,
                                        })


def services(request):
    pg_name = 'services'
    return render(request, 'services.html', {'pg_name': pg_name})


def oil_change_packages(request):
    pg_name = 'oil-change-packages'
    return render(request, 'services/oil-change-packages.html', {'pg_name': pg_name})


def check_is_open():
    from django.utils import timezone
    import datetime
    
    current_datetime = timezone.localtime(timezone.now())
    current_weekday = timezone.localtime(timezone.now()).strftime("%A")
    opens_at = current_datetime.replace(hour=7, minute=30)
    weekday_closes_at = current_datetime.replace(hour=16, minute=30)
    saturday_closes_at = current_datetime.replace(hour=13, minute=00)
    if ((current_weekday not in ['Saturday', 'Sunday'] and opens_at <= current_datetime < weekday_closes_at)
            or (current_weekday in ['Saturday'] and opens_at <= current_time < saturday_closes_at)):
        is_open = True
    else:
        is_open = False
    return is_open
    return is_open
