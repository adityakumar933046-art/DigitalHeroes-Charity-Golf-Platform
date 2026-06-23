from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.plans,
        name='plans'
    ),

    path(
        'subscribe/<str:plan>/',
        views.subscribe,
        name='subscribe'
    ),

    path(
        'payment-success/',
        views.payment_success,
        name='payment_success'
    ),

    path(
        'status/',
        views.subscription_status,
        name='subscription_status'
    ),

]