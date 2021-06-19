from django.contrib import admin
from .models import Feed
# from .models import User
# Register your models here.
# class UserAdmin(admin.ModelAdmin) :
#     list_display = ('username', 'password')

admin.site.register(Feed)
# admin.site.register(User, UserAdmin) #site에

