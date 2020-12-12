from django.urls import path
from . import views

urlpatterns = [
    path('',views.membership),
    path('success/',views.success),
    path('premiers/',views.RanNumGen),
]
