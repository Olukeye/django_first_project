from django.urls import path
from .views import BlogListView, BlogDetailView
from . import views


urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),     #rather than use the usual convention "path('', views.home, name='home')"
    path('post/<str:pk>', views.BlogDetailView.as_view(), name='blogger-detail'),  
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('posts/<str:pk>', views.singleblog, name='posts')
]
