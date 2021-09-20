from django.urls import path

from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),
    path('meetups/success', views.confirm_registration, name='confirm-registration'),
    # domain/meetup
    path('meetups/<slug:meetup_slug>/', views.meetup_details, name='meetup-detail'),
    # domain/meetups/<dynamic-path-segment>
]
