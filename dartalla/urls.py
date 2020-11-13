from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('user.urls')),
    path('', include('dashboard.urls')),
    path('', include('person.urls')),
]
