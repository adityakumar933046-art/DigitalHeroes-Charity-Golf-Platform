from django.contrib import admin
from .models import Charity, UserCharity

admin.site.register(Charity)
admin.site.register(UserCharity)