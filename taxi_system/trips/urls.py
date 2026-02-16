from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashbord, name='dashbord'),
    path('start/', views.start_trip, name='start_trip'),
    path('end/<int:trip_id>/', views.end_trip, name='end_trip'),
    path('history/', views.trip_history, name='trip_history'),
]
