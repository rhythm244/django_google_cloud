from django.contrib import admin
from django.urls import include, path

# from myapp.view_api import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('herc_admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
