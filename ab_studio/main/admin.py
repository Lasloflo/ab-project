from django.contrib import admin
from .models import *
# Register your models here.

class PhotoInHomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'text_on_left') # отображение полей объектов в списке в админке
    list_display_links = ('title', 'description', 'photo') # ссылки для редактирования
    list_editable = ('text_on_left',) # редактирование в списке объектов

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'created_at', 'is_publish')
    list_display_links = ('title', 'description', 'photo')
    list_editable = ('is_publish',)
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title",)}


class PhotoAlbumsAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'album')
    list_display_links = ('photo',)
    list_editable = ('album',)


admin.site.register(PhotoInHomePage, PhotoInHomePageAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(PhotoAlbums, PhotoAlbumsAdmin)
