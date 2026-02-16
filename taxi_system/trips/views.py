from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum

from accounts.models import Driver
from .models import Trip
from .forms import StartTripForm, EndTripForm


# Create your views here. 
#Driver Dashboard
@login_required
def dashbord(request):
    conductor = get_object_or_404(Driver, usario=request.user)

    today_trips = Trip.objects.filter(conductor=conductor,
        hora_inicio__date=timezone.now().date(),
        estatuto='completado')
    
    total_earnings = today_trips.aggregate(Sum('dinero'))['dinero__sum'] or 0
    active_trip = Trip.objects.filter(
        conductor=conductor,
        estatuto='en curso'
    ).first()

    return render(request, 'trips/dashboard.html', {
        'total_earnings': total_earnings,
        'today_trips': today_trips.count(),
        'active_trip': active_trip
    })
# Start Trip
@login_required
def start_trip(request):
    conductor = get_object_or_404(Driver, usario=request.user)

    if Trip.objects.filter(conductor=conductor, estatuto='en curso').exists():
        return redirect('dashbord')

    if request.method == 'POST':
        form = StartTripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.conductor = conductor
            trip.estatuto = 'en curso'
            trip.save()
            return redirect('dashbord')
    else:
        form = StartTripForm()

    return render(request, 'trips/start_trip.html', {'form': form})
# End Trip
@login_required
def end_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, estatuto='en curso')

    if request.method == 'POST':
        form = EndTripForm(request.POST, instance=trip)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.hora_fin = timezone.now()
            trip.estatuto = 'completado'
            trip.save()
            return redirect('dashbord')
    else:
        form = EndTripForm(instance=trip)

    return render(request, 'trips/end_trip.html', {'form': form})
#Trip History
@login_required
def trip_history(request):
    conductor = get_object_or_404(Driver, usario=request.user)
    trips = Trip.objects.filter(conductor=conductor).order_by('-hora_inicio')
    total_earnings = trips.aggregate(Sum('dinero'))['dinero__sum'] or 0
    return render(request, 'trips/history.html', {'trips': trips, 'total_earnings': total_earnings})


