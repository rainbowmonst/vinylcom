from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('artist', 'release_year', 'price', 'genres')
    search_fields = ('artist', 'genres')
    list_filter = ('release_year', 'genres')