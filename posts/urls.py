from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('new_post/', views.new_post, name="new_post"),
    path('contact', views.contact, name="contact"),
    path('post/<int:id>', views.post_detail, name='post_detail')
    
]