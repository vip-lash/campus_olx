from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices
from django.contrib.auth.decorators import login_required
from listings.models import Listing
from team_members.models import Team

def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    team_members = Team.objects.order_by('-join_date')
    context = {
    'team_members': team_members}

    return render(request, 'pages/about.html',context)
