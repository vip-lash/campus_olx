from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices
from .models import Listing
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
      'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
      'listing': listing
  }

  return render(request, 'listings/listing.html', context)


def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
      'price_choices': price_choices,
      'listings': queryset_list,
      'values': request.GET
  }

  return render(request, 'listings/search.html', context)

@login_required(login_url='login')
def sell_items(request):
  if request.method == 'POST':
    title = request.POST['title']
    price = request.POST['price']
    description = request.POST['description']
    photo_main=request.FILES['photo_main']
    print(photo_main.name)
    photo_1 = request.FILES.get('photo_1',False)
    photo_2 = request.FILES.get('photo_2', False)
    photo_3 = request.FILES.get('photo_3', False)
    user_id = request.user.id
    seller=request.POST['seller']
    phone = request.POST.get('phone',False)


    listing = Listing(title=title, price=price,
                      description=description, photo_main=photo_main, photo_1=photo_1,
                      photo_2=photo_2, photo_3=photo_3, user_id=user_id, seller=seller, phone=phone)
    listing.save()
    messages.success(request, 'Your item is now listed')

  return render(request, 'listings/sell.html')




 
 
