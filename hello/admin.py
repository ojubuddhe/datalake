from django.contrib import admin
from .models import User, lostdeposit

# Register your models here.

admin.site.register(User)

admin.site.register(lostdeposit)

