from django.contrib import admin
from .models import Post
from .models import Color

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

class ColorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Color, ColorAdmin)
