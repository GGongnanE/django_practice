from django.contrib import admin
from .models import Board

# Register your models here.
# admin.site.register(Board)

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['title', 'like_count']
    list_display_links = ['title','like_count']