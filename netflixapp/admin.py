from django.contrib import admin
from netflixapp.models import Profile, Movie, Video, CustomUser

# Register your models here.
admin.site.register(Movie)
admin.site.register(Video)
admin.site.register(Profile)
admin.site.register(CustomUser)
