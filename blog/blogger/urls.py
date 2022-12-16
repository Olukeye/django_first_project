from django.urls import path
from .views import PostListView, PostDetailView
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),     #rather than use the usual convention "path('', views.home, name='home')"
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('posts/<str:pk>', views.singleblog, name='posts')
]
