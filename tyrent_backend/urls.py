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
    path('api/users/', include('users.urls')),
    path('api/properties/', include('properties.urls')),
    path('api/wallet/', include('wallet.urls')),
    path('api/bookings/', include('bookings.urls')),

    # Existing sitemap 
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
