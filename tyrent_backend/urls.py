from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls_auth')),
    path('api/admin/', include('users.urls_admin')),
    path('api/users', include('users.urls_users')),
    path('api/landlord/', include('users.urls_landlord')),
    path('api/tenant/', include('users.urls_tenant')),


    path('properties/', include('properties.urls')),
    path('wallet/', include('wallet.urls')),
    path('bookings/', include('bookings.urls')),
]
