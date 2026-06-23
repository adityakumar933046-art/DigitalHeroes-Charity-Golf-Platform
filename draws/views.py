from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Draw
from datetime import date
import random


def draw_list(request):

    draws = Draw.objects.filter(
        is_published=True
    ).order_by('-year', '-month')

    return render(
        request,
        'draws/list.html',
        {'draws': draws}
    )


@staff_member_required
def generate_draw(request):

    today = date.today()

    numbers = random.sample(range(1, 51), 5)

    Draw.objects.create(
        month=today.month,
        year=today.year,

        number1=numbers[0],
        number2=numbers[1],
        number3=numbers[2],
        number4=numbers[3],
        number5=numbers[4],

        draw_type='random',
        is_published=True
    )

    return redirect('/draws/')