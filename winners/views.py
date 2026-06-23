from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Winner

def winner_list(request):


    search = request.GET.get('q')

    winners = Winner.objects.all().order_by(
    '-winning_date'
)

    if search:

        winners = winners.filter(
        name__icontains=search
    )

    paginator = Paginator(
    winners,
    6
)

    page = request.GET.get('page')

    winners = paginator.get_page(page)

    return render(
    request,
    'winners/list.html',
    {
        'winners': winners,
        'search': search,
    }
)

