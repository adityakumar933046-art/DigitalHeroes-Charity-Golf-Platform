from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import date, timedelta
import razorpay

from .models import Subscription, Payment


@login_required
def plans(request):

    return render(
        request,
        'subscriptions/plans.html'
    )


@login_required
def subscribe(request, plan):

    if plan == "monthly":
        amount = 999

    elif plan == "yearly":
        amount = 9999

    else:
        return redirect('/subscriptions/')

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    order = client.order.create({
        "amount": amount * 100,
        "currency": "INR",
        "payment_capture": 1
    })

    Payment.objects.create(
        user=request.user,
        razorpay_order_id=order["id"],
        amount=amount,
        status="pending"
    )

    return render(
        request,
        "subscriptions/payment.html",
        {
            "order_id": order["id"],
            "amount": amount,
            "plan": plan,
            "key": settings.RAZORPAY_KEY_ID
        }
    )


@login_required
def payment_success(request):

    if request.method == "POST":

        payment_id = request.POST.get(
            "razorpay_payment_id"
        )

        order_id = request.POST.get(
            "razorpay_order_id"
        )

        plan = request.POST.get(
            "plan"
        )

        payment = Payment.objects.get(
            razorpay_order_id=order_id
        )

        payment.razorpay_payment_id = payment_id
        payment.status = "success"
        payment.save()

        start_date = date.today()

        if plan == "monthly":

            end_date = start_date + timedelta(days=30)

        else:

            end_date = start_date + timedelta(days=365)

        Subscription.objects.update_or_create(
            user=request.user,
            defaults={
                'plan': plan,
                'start_date': start_date,
                'end_date': end_date,
                'is_active': True,
            }
        )

        return redirect('/dashboard/')

    return redirect('/subscriptions/')


@login_required
def subscription_status(request):

    subscription = None

    try:

        subscription = Subscription.objects.get(
            user=request.user
        )

        if subscription.end_date < date.today():

            subscription.is_active = False
            subscription.save()

    except Subscription.DoesNotExist:

        pass

    return render(
        request,
        'subscriptions/status.html',
        {
            'subscription': subscription
        }
    )