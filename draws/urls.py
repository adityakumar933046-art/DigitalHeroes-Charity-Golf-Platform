from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.draw_list,
        name='draws'
    ),

    path(
        'generate/',
        views.generate_draw,
        name='generate_draw'
    ),

]