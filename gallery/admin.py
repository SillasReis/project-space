from django.contrib import admin

from gallery.models import Photo


class ListPhotos(admin.ModelAdmin):
    list_display = ('id', 'name', 'subtitle', 'created_at', 'is_published', 'user')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'user')
    list_filter = ('category', 'user')
    list_editable = ('is_published',)
    list_per_page = 10

admin.site.register(Photo, ListPhotos)
