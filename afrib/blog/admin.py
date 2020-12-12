from django.contrib import admin

# Register your models here.
from .models import gallery
class GalleryAdmin(admin.ModelAdmin):
    list_displays = ['Img']

admin.site.register(gallery, GalleryAdmin)
