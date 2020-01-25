from django.contrib import admin
from profilemaker.models import User_Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display =['fname','lname','technologies','email','display_picture']

admin.site.register(User_Profile,ProfileAdmin)