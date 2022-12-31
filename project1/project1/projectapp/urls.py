from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    #path('add/',views.addition,name='addition'),
    #path('demo/',views.prgdemo,name='prgdemo'),
    #path('about/',views.about,name='about'),
    #path('contact/',views.contact, name='contact'),
    #path('detail/',views.detail,name='detail'),
    #path('thanks/',views.thanks,name='thanks')
]
