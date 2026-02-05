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
    path('users/', include('users.urls')),
    path('properties/', include('properties.urls')),
    path('wallet/', include('wallet.urls')),
    path('bookings/', include('bookings.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
