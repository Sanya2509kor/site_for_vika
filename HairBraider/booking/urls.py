from django.urls import path
from booking import views

app_name = 'booking'

urlpatterns = [
    path('', views.BookingView.as_view(), name='booking'),
]
