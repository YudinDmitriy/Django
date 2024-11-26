from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm, ProductModerForm, ProductContentManageForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.services.services import get_categories_from_cache
from users.models import User


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        for obj in context["object_list"]:
            if Version.objects.filter(product=obj).last():
                obj.active_version = (
                    Version.objects.filter(product=obj, current_version_indicator=True)
                    .last()
                    .version_name
                )
                obj.num_version = (
                    Version.objects.filter(product=obj, current_version_indicator=True)
                    .last()
                    .version_number
                )
                obj.save()

        context['categories'] = get_categories_from_cache()

        return context


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            print(f"{name[0]}({phone[0]}):{message}")
        return HttpResponseRedirect("/contacts")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = "users:login"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product:list")
    login_url = "users:login"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.creator = self.request.user
            self.object.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product:list")
    login_url = "users:login"
    perms = ('catalog.can_edit_activity', 'catalog.can_edit_description', 'catalog.can_edit_category')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.creator or user.is_superuser:
            return ProductForm
        if user.has_perms(perm_list=self.perms):
            return ProductModerForm
        if user.has_perm('catalog.can_edit_activity'):
            return ProductContentManageForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("product:list")
    login_url = "users:login"
