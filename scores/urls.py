from django.urls import path
from . import views

urlpatterns = [

    path(
        'add/',
        views.add_score,
        name='add_score'
    ),

    path(
        'list/',
        views.score_list,
        name='score_list'
    ),

    path(
        'edit/<int:score_id>/',
        views.edit_score,
        name='edit_score'
    ),

    path(
        'export/',
        views.export_scores,
        name='export_scores'
    ),

    path(
        'leaderboard/',
        views.leaderboard,
        name='leaderboard'
    ),
    path(
    'delete/<int:score_id>/',
    views.delete_score,
    name='delete_score'
),

]