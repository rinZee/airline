from django.shortcuts import render

from .models import Flight
# Create your views here.
def flight(request, flight_id):
	flight = Flight.objects.get(pk=flight_id)
	return render(request, "flights/flight.html", {
		"flight": flight
	})

def index(request):
	return render(request, "flights/index.html", {
		"flights": Flight.objects.all()
	})