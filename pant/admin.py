from django.contrib import admin

# Register your models here.

from .models import Category, Announcement, Link

#admin.site.register(Category) 
admin.site.register(Announcement)
admin.site.register(Link)