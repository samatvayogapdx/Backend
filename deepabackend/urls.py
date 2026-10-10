
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('UserApp.urls')),
    path('calendar/', include('CalendarApp.urls'))
]
