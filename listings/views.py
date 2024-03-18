from django.shortcuts import render
from .models import Listing
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from choices import bedroom_choices, state_choices, price_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    context = {
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices
    }
    return render(request, 'listings/search.html', context)
