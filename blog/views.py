from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog
    

