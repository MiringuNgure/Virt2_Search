from django.shortcuts import render
from .models import Airport_data
from .forms import AirportSearchForm


def index(request):
    results = Airport_data.objects.all()
    return render(request, "index.html", {"data":results})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html") 

def search(request):
    form = AirportSearchForm

    results = []
    if 'q' in request.GET:
        form = AirportSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Airport_data.objects.filter(name__contains= q)

    return render(request, "search.html", {'form':form, 'results':results})