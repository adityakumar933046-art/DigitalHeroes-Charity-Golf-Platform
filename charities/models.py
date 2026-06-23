from django.db import models

class Charity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='charity_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class UserCharity(models.Model):
    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE
    )

    charity = models.ForeignKey(
        Charity,
        on_delete=models.CASCADE
    )

    donation_percentage = models.IntegerField(default=10)

    def __str__(self):
        return self.user.username