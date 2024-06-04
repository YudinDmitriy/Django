from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    product = Product.objects.all()
    context = {"products": product}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    one_product = get_object_or_404(Product, pk=pk)
    context = {"product": one_product}
    return render(request, 'catalog/product_detail.html', context)
