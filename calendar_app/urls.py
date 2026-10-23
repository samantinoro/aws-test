from django.contrib import admin
from django.urls import path, include
from .views import calendar_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calendar_app.urls')),
path('', calendar_view, name='calendar)
]
