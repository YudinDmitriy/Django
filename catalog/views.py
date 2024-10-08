from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:list')
