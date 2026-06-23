from django.db import models


class Draw(models.Model):

    DRAW_TYPES = (
        ('random', 'Random'),
        ('algorithm', 'Algorithm'),
    )

    month = models.IntegerField()
    year = models.IntegerField()

    number1 = models.IntegerField()
    number2 = models.IntegerField()
    number3 = models.IntegerField()
    number4 = models.IntegerField()
    number5 = models.IntegerField()

    draw_type = models.CharField(
        max_length=20,
        choices=DRAW_TYPES,
        default='random'

    )
    is_simulation = models.BooleanField(
        default=True
    )


    is_published = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.month}/{self.year}"


class PrizePool(models.Model):

    total_pool = models.IntegerField(
        default=10000
    )

    def five_match_prize(self):
        return self.total_pool * 40 / 100

    def four_match_prize(self):
        return self.total_pool * 35 / 100

    def three_match_prize(self):
        return self.total_pool * 25 / 100

    def __str__(self):
        return f"Pool ₹{self.total_pool}"