from django.urls import path

from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_activity

app_name = 'blog'
urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>', toggle_activity, name='activity'),

]
