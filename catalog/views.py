from django.http import HttpResponseRedirect
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView


class HomeListView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Контакты"
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name'),
            phone = request.POST.get('phone'),
            message = request.POST.get('message')
            print(f'{name[0]}({phone[0]}):{message}')
        return HttpResponseRedirect('/contacts')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
