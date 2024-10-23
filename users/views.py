from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UsersRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UsersRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user