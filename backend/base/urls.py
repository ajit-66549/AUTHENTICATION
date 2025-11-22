from django.urls import path

from .views import getnote, CustomTokenObtain, CustomRefreshToken

urlpatterns = [
    path('token/', CustomTokenObtain.as_view(), name="access_token"),
    path('token/refresh/', CustomRefreshToken.as_view(), name="refresh_token"),
    path('notes/', getnote, name="notes"),
]
