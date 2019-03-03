from django.shortcuts import render


# Views
def home(request):
    pg_name = 'home'
    is_open = check_is_open()
    return render(request, 'home.html', {
                                            'is_open': is_open,
                                            'pg_name': pg_name,
                                        })


def privacy_policy(request):
    pg_name = 'privacy-policy'
    return render(request, 'privacy-policy.html', {'pg_name': pg_name})


def services(request):
    pg_name = 'services'
    return render(request, 'services.html', {'pg_name': pg_name})


def oil_change_packages(request):
    pg_name = 'oil-change-packages'
    return render(request, 'services/oil-change-packages.html', {'pg_name': pg_name})


def brake_services(request):
    pg_name = 'brake-services'
    return render(request, 'services/brake-services.html', {'pg_name': pg_name})


def suspension_services(request):
    pg_name = 'suspension-services'
    return render(request, 'services/suspension-services.html', {'pg_name': pg_name})


def tires_wheels(request):
    pg_name = 'tires-wheels'
    return render(request, 'services/tires-wheels.html', {'pg_name': pg_name})


def road_trip(request):
    pg_name = 'road-trip'
    return render(request, 'services/road-trip.html', {'pg_name': pg_name})


def prepurchase_ins(request):
    pg_name = 'prepurchase-ins'
    return render(request, 'services/prepurchase-ins.html', {'pg_name': pg_name})


def major_service(request):
    pg_name = 'major-service'
    return render(request, 'services/major-service.html', {'pg_name': pg_name})


def check_is_open():
    from django.utils import timezone
    
    current_datetime = timezone.localtime(timezone.now())
    current_weekday = timezone.localtime(timezone.now()).strftime("%A")
    opens_at = current_datetime.replace(hour=7, minute=30)
    weekday_closes_at = current_datetime.replace(hour=17, minute=00)
    saturday_closes_at = current_datetime.replace(hour=13, minute=30)
    if ((current_weekday not in ['Saturday', 'Sunday'] and opens_at <= current_datetime < weekday_closes_at)
            or (current_weekday in ['Saturday'] and opens_at <= current_datetime < saturday_closes_at)):
        is_open = True
    else:
        is_open = False
    return is_open
