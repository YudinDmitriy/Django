from django.urls import path

from blog.views import BlogCreateView, BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    # path('blog/<int:pk>', ...DetailView.as_view(), `name=`'blog_detail'),
    # path('edit/<int:pk>', ...UpdateView.as_view(), name='blog_Update'),
    # path('delete/<int:pk>', ...DeleteView.as_view(), name='blog_Delete'),

]
