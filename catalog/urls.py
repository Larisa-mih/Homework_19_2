from django.urls import path
from catalog.views import (index_contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='index_home'),
    path('contacts/', index_contacts, name='index_contacts'),
    path('<int:pk>/catalog/', ProductDetailView.as_view(), name="product"),
    path('create/', ProductCreateView.as_view(), name="create_product"),
    path('update/<int:pk>', ProductUpdateView.as_view(), name="update_product"),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name="delete_product"),

]
