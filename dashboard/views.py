from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.db.models import Sum

from scores.models import Score
from charities.models import UserCharity, Charity
from winners.models import Winner
from draws.models import Draw
from subscriptions.models import Subscription

User = get_user_model()


def home(request):

    latest_winners = Winner.objects.order_by(
        '-winning_date'
    )[:3]

    return render(
        request,
        'dashboard/home.html',
        {
            'latest_winners': latest_winners
        }
    )


@login_required
def dashboard(request):

    scores = Score.objects.filter(
        user=request.user
    ).order_by('-played_on')[:5]

    total_scores = Score.objects.filter(
        user=request.user
    ).count()

    selected_charity = None
    donation_percentage = None

    try:

        user_charity = UserCharity.objects.get(
            user=request.user
        )

        selected_charity = user_charity.charity
        donation_percentage = user_charity.donation_percentage

    except UserCharity.DoesNotExist:

        pass

    subscription = None

    try:

        subscription = Subscription.objects.get(
            user=request.user
        )

    except Subscription.DoesNotExist:

        pass

    total_winners = Winner.objects.count()
    total_draws = Draw.objects.count()
    total_charities = Charity.objects.count()



    draws_entered = total_scores

    

    total_won = Winner.objects.filter(
        name=request.user.username
    ).aggregate(
        Sum('prize_amount')
    )['prize_amount__sum'] or 0

    payment_status = "Pending"

    latest_win = Winner.objects.filter(
        name=request.user.username
    ).order_by('-winning_date').first()

    if latest_win:

        payment_status = latest_win.payment_status

    score_data = Score.objects.filter(
        user=request.user
    ).order_by('played_on')

    score_dates = [
        score.played_on.strftime("%d-%b")
        for score in score_data
    ]

    score_values = [
        score.score
        for score in score_data
    ]

    context = {

        'scores': scores,
        'total_scores': total_scores,

        'selected_charity': selected_charity,
        'donation_percentage': donation_percentage,

        'subscription': subscription,

        'total_winners': total_winners,
        'total_draws': total_draws,
        'total_charities': total_charities,

        'draws_entered': draws_entered,
        'total_won': total_won,
        'payment_status': payment_status,

        'score_dates': score_dates,
        'score_values': score_values,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )


@staff_member_required
def admin_analytics(request):

    context = {
        'total_users': User.objects.count(),
        'total_scores': Score.objects.count(),
        'total_winners': Winner.objects.count(),
        'total_draws': Draw.objects.count(),
        'total_charities': Charity.objects.count(),
    }

    return render(
        request,
        'dashboard/admin_analytics.html',
        context
    )