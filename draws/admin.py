from django.contrib import admin
from .models import Draw, PrizePool

@admin.register(Draw)
class DrawAdmin(admin.ModelAdmin):


    list_display = (
    'month',
    'year',
    'draw_type',
    'is_simulation',
    'is_published'
)

    list_filter = (
    'draw_type',
    'is_simulation',
    'is_published'
)

    search_fields = (
    'month',
    'year'
)


@admin.register(PrizePool)
class PrizePoolAdmin(admin.ModelAdmin):


    list_display = (
    'total_pool',
)

