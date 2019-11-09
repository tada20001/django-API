from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expert/', include('expert.urls')),
    path('ep03/', include('ep03.urls')),
]
