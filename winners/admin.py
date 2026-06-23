from django.contrib import admin
from .models import Winner

@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):


    list_display = (
    'name',
    'prize_amount',
    'winning_date',
    'verification_status',
    'payment_status',
)

    list_filter = (
    'verification_status',
    'payment_status',
)

    search_fields = (
    'name',
)

