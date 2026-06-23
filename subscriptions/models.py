from django.db import models
from django.conf import settings
from django.utils import timezone
timezone.now

class Subscription(models.Model):


    PLAN_CHOICES = (
    ('monthly', 'Monthly'),
    ('yearly', 'Yearly'),
)

    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
)

    plan = models.CharField(
    max_length=20,
    choices=PLAN_CHOICES
)

    start_date = models.DateField()

    end_date = models.DateField()

    is_active = models.BooleanField(
    default=True
)

def __str__(self):
    return f"{self.user.username} - {self.plan}"


class Payment(models.Model):


    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE
)

    razorpay_order_id = models.CharField(
    max_length=200
)

    razorpay_payment_id = models.CharField(
    max_length=200,
    blank=True,
    null=True
)

    amount = models.IntegerField(default = 0)

    status = models.CharField(
    max_length=20,
    default='pending'
)

    created_at = models.DateTimeField(
    auto_now_add=True
)

def __str__(self):
    return f"{self.user.username} - ₹{self.amount}"

