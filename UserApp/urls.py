from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path,include
from .views import *

urlpatterns = [
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('token/refresh',TokenRefreshView.as_view(), name='token_refresh' ),
]
#username   deepa
#password sT@rbucks