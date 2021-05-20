from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from listings.models import Listing
from django.contrib.auth.decorators import login_required



def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(
              username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')


def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')


@login_required(login_url='login')
def dashboard(request):
  user_contacts = Contact.objects.order_by(
      '-contact_date').filter(user_id=request.user.id)

  context = {
      'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def delete_inquiry(request, id):
  item_query = Contact.objects.get(pk=id)
  item_query.delete()
  return redirect('dashboard')


@login_required(login_url='login')
def my_listings(request):
  user_listings = Listing.objects.order_by(
      '-list_date').filter(user_id=request.user.id)
  
  context = {
      'listings': user_listings
  }
  return render(request, 'accounts/ads.html', context)


@login_required(login_url='login')
def delete_listing(request, id):
  item_query = Listing.objects.get(pk=id)
  item_query.delete()
  return redirect('my_listings')
