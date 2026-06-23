from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.charity_list,
        name='charities'
    ),

    path(
        'select/<int:charity_id>/',
        views.select_charity,
        name='select_charity'
    ),

]