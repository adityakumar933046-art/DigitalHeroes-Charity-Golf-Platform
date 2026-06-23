from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
import csv
from django.shortcuts import render, redirect, get_object_or_404
from .models import Score

def leaderboard(request):


    leaders = (
    Score.objects
    .values('user__username')
    .annotate(total_score=Sum('score'))
    .order_by('-total_score')
)

    return render(
    request,
    'scores/leaderboard.html',
    {'leaders': leaders}
)


@login_required
def add_score(request):


    if request.method == "POST":

        score = request.POST.get("score")
        played_on = request.POST.get("played_on")

    if Score.objects.filter(
        user=request.user,
        played_on=played_on
    ).exists():

        return render(
            request,
            'scores/add_score.html',
            {
                'error': 'Score already exists for this date.'
            }
        )

    Score.objects.create(
        user=request.user,
        score=score,
        played_on=played_on
    )

    scores = Score.objects.filter(
        user=request.user
    ).order_by('-played_on')

    if scores.count() > 5:

        oldest_score = scores.last()
        oldest_score.delete()

    return redirect('/scores/list/')

    return render(
    request,
    'scores/add_score.html'
)


@login_required
def score_list(request):


    scores = Score.objects.filter(
    user=request.user
).order_by('-played_on')

    return render(
    request,
    'scores/score_list.html',
    {'scores': scores}
)

@login_required
def edit_score(request, score_id):

    score = get_object_or_404(
        Score,
        id=score_id,
        user=request.user
    )

    if request.method == "POST":

        score.score = request.POST.get("score")
        score.played_on = request.POST.get("played_on")

        score.save()

        return redirect('/scores/list/')

    return render(
        request,
        'scores/edit_score.html',
        {
            'score': score
        }
    )

@login_required
def delete_score(request, score_id):

    score = get_object_or_404(
        Score,
        id=score_id,
        user=request.user
    )

    score.delete()

    return redirect(
        '/scores/list/'
    )

@login_required
def export_scores(request):


    response = HttpResponse(
    content_type='text/csv'
)

    response[
    'Content-Disposition'
] = 'attachment; filename="scores.csv"'

    writer = csv.writer(response)

    writer.writerow([
    'Score',
    'Date'
])

    scores = Score.objects.filter(
    user=request.user
)

    for score in scores:

        writer.writerow([
        score.score,
        score.played_on
    ])

    return response

