from django.contrib import admin
from users.models import Review, CustomUser
# # Register your models here.

admin.site.register(Review)
admin.site.register(CustomUser)
