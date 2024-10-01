from django.urls import path

from catalog.views import ContactsTemplateView,  ProductDetailView, HomeListView

urlpatterns = [
    path('', HomeListView.as_view()),
    path('contacts/', ContactsTemplateView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail')

]
