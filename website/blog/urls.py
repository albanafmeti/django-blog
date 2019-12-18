from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.get_all, name="all-blog"),
    path('posts/<int:post_id>/', views.show, name="single-post"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('contact/send', views.contact_send, name="contact-send"),
]
