from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import index_home, index_contacts
urlpatterns = [
    path('contacts/', index_contacts),
    path('', index_home)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
