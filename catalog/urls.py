from django.urls import path
from catalog.views import index_home, index_contacts
urlpatterns = [
    path('contacts/', index_contacts),
    path('', index_home)
]
