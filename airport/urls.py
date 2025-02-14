"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flights.views import FlightsListViews, BookingsListViews, BookingDetailsViews
from users.views import UserCreateAPIView, UserLoginAPIView, BookingCreateAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flights/", FlightsListViews.as_view(), name="flights_list"),
    path("bookings/", BookingsListViews.as_view(), name= "bookings_list"),
    path("details/<int:booking_id>/", BookingDetailsViews.as_view(), name="details"),
    
    # here create and login paths

    path("create/", UserCreateAPIView.as_view(), name="create"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
    path("book-flight/<int:flight_id>/", BookingCreateAPIView.as_view(), name="book-flight"),


]
