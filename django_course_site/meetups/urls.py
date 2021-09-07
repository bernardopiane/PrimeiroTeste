from django.urls import path

from . import views

urlpatterns = [
    path('meetups/', views.index),  # domain/meetup
    path('meetups/<slug:meetup_slug>/', views.meetup_details)  # domain/meetups/<dynamic-path-segment>
]
