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



    path('api/properties/', include('properties.urls')),
    path('api/units/', include('properties.urls')),
    path('api/apartments/', include('properties.urls')),
    path('api/wallet/', include('wallet.urls')),
    path('api/bookings/', include('bookings.urls')),

    path('api/sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
