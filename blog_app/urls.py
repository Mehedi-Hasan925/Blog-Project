from django.urls import path
from blog_app import views

app_name='blog_app'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create_blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('update_blog/<pk>', views.UpdateBlog.as_view(), name='update_blog'),
    path('blog_detail/<slug:slug>/', views.BlogDetail, name='blog_detail'),
    path('my_blog/', views.MyBlog.as_view(), name='my_blog'),
    path('liked/<int:pk>/', views.Liked, name='liked'),
    path('unliked/<int:pk>/', views.unliked, name='unliked'),
    
  
]