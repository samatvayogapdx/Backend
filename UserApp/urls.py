from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),    
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('token/refresh',TokenRefreshView.as_view(), name='token_refresh' ),
    path('intake-form/', SubmitForm.as_view(), name='intake-form')
]
