from django.contrib import admin

from .models import User, SalesRep, Prospect

admin.site.register(User)
admin.site.register(SalesRep)
admin.site.register(Prospect)