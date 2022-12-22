from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, UserBlogListView
from . import views


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),     #rather than use the usual convention "path('', views.home, name='home')"
    path('user/<str:username>', UserBlogListView.as_view(), name='user-blogs'),
    path('post/<str:pk>', BlogDetailView.as_view(), name='blogger-detail'),
    path('post/<str:pk>/update', BlogUpdateView.as_view(), name='blogger-update'), 
    path('post/<str:pk>/delete', BlogDeleteView.as_view(), name='blogger-delete'), 
    path('post/new/', BlogCreateView.as_view(), name='blogger-create'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('posts/<str:pk>', views.singleblog, name='posts')
]
