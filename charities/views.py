from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Charity, UserCharity


@login_required
def charity_list(request):

    search = request.GET.get(
        'search',
        ''
    )

    charities = Charity.objects.all()

    if search:

        charities = charities.filter(
            name__icontains=search
        )

    return render(
        request,
        'charities/list.html',
        {
            'charities': charities,
            'search': search
        }
    )


@login_required
def select_charity(request, charity_id):

    charity = Charity.objects.get(
        id=charity_id
    )

    UserCharity.objects.update_or_create(
        user=request.user,
        defaults={
            'charity': charity
        }
    )

    return redirect(
        '/dashboard/'
    )