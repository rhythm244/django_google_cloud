from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('herc_admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
