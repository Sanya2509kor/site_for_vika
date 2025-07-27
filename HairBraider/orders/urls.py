from django.urls import path
from orders import views


app_name = 'order'

urlpatterns = [
    path('appointment/', views.AppointmentView.as_view(), name='appointment'),
    path('ajax/load-times/', views.load_times, name='ajax_load_times'),
    # path('success/', views.success_view, name='success_page'),
]