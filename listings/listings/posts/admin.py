from django.contrib import admin
from .models import Language, Post, Tool

# Register your models here.
admin.site.register(Language)
admin.site.register(Post)
admin.site.register(Tool)