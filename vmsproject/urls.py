from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^$',  views.about, name="about"),
    url(r'^$',  views.contact, name="contact"),
    url(r'^$',  views.service, name="services"),
    url(r'^$',  views.products, name="services"),
    url(r'^$',  views.thank, name="thank"),
]

# urlpatterns = [
#     path("", views.index, name="home"),
#     path("about", views.about, name="about"),
#     path("contact", views.contact, name="contact"),
#     path("service", views.service, name="services"),
#     path("products", views.products, name="services"),
#     path("thanks", views.thank, name="thank"),
  
# ]
