from  django.urls import path

from .urls_auth import urlpatterns
from .views import landlord_dashboard


urlpatterns = [
path('dashboard', landlord_dashboard, name='landlord-dashboard'),
#path('documents/upload', upload_landlord_documents, name='landlord-documents-upload'),

]