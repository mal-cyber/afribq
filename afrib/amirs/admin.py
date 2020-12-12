from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import main_amirs,members,premiers,ran
# Register your models here.

admin.site.register(main_amirs)
admin.site.register(members)
admin.site.register(premiers)
admin.site.register(ran)
