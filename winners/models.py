from django.db import models

class Winner(models.Model):


    VERIFICATION_STATUS = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
)

    PAYMENT_STATUS = (
    ('Pending', 'Pending'),
    ('Paid', 'Paid'),
)

    name = models.CharField(
    max_length=100,
    default="Winner"
)

    prize_amount = models.IntegerField(
    default=0
)

    winning_date = models.DateField(
    default="2026-01-01"
)

    proof_image = models.ImageField(
    upload_to='winner_proofs/',
    blank=True,
    null=True
)

    verification_status = models.CharField(
    max_length=20,
    choices=VERIFICATION_STATUS,
    default='Pending'
)

    payment_status = models.CharField(
    max_length=20,
    choices=PAYMENT_STATUS,
    default='Pending'
)

def __str__(self):
    return self.name

