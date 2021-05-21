from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    username = request.POST['username']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(
          listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(
            request, 'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name,
                      email=email, phone=phone, message=message, user_id=user_id, username=username)

    contact.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(
        request, 'Your request has been submitted')
    return redirect('/listings/'+listing_id)
