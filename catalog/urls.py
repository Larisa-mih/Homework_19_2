from django.urls import path
from catalog.views import index_contacts, ProductListView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index_home'),
    path('contacts/', index_contacts, name='index_contacts'),
    path('<int:pk>/catalog/', ProductDetailView.as_view(), name="product"),
]
