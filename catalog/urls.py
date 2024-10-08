from django.urls import path

from catalog.views import ContactsTemplateView, ProductDetailView, ProductCreateView, ProductListView, \
    ProductUpdateView, ProductDeleteView

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),

]
