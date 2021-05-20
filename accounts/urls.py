from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('delete_inquiry/<int:id>', views.delete_inquiry, name='delete_inquiry'),
    path('delete_listing/<int:id>', views.delete_listing, name='delete_listing'),
    path('my_listings', views.my_listings, name='my_listings'),


]
