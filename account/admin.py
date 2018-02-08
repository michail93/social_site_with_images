from django.contrib import admin

# Register your models here.
from .models import Profile



class ProfileAdmin(admin.ModelAdmin):
    list_dispaly=['user', 'date_of_bird', 'photo']



admin.site.register(Profile, ProfileAdmin)

    
