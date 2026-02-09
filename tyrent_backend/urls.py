from django.contrib import admin
from django.urls import path, include 
from django.contrib.sitemaps.views import sitemap
from properties.sitemaps import ApartmentSitemap, UnitSitemap

sitemaps = {
    'apartments': ApartmentSitemap,
    'units': UnitSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls_auth')),
    path('api/admin/', include('users.urls_admin')),
    path('api/users/', include('users.urls_users')),
    path('api/landlord/', include('users.urls_landlord')),
    path('api/tenant/', include('users.urls_tenant')),


    path('properties/', include('properties.urls')),
    path('wallet/', include('wallet.urls')),
    path('bookings/', include('bookings.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
