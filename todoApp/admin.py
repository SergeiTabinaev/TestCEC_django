from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(UserApp, UserAdmin) #UserAccount
admin.site.register(Category)
admin.site.register(Task)

