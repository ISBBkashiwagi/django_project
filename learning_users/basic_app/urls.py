from django.conf.urls import url
from django.urls import path
from basic_app import views

# TEMPLATE URLS!
app_name = 'basic_app'

urlpatterns=[
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('post/create', views.create_post, name='create_post'),
    path('post/show', views.show_post, name='show_post'),
    path('post/<int:pk>/edit', views.edit_post, name='edit_post'),
    path('post/<int:pk>/delete', views.delete_post, name='delete_post'),
]   