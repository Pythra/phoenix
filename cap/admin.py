from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, Announcement, Post, Wallet, Deposit, Plans

admin.site.register(Profile)
admin.site.register(Announcement)
admin.site.register(Post) 
admin.site.register(Wallet)
admin.site.register(Deposit)
admin.site.register(Plans)
