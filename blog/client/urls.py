from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post2', views.post2, name='post2'),
    path('post3', views.post3, name='post3'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
