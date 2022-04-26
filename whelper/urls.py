from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('sysinfo',views.sysinfo1,name="sysinfo"),
    path('S1',views.sysinfo,name="sysinfo"),
    path('homey',views.home,name="home"),
    path('rest_sys_info',views.sys_health,name="sys_health"),
    path('internet_speed',views.internet_speed,name="internet_speed"),
    path('url_status_input',views.url_status_input,name="url_status_input"),
    path('url_status',views.url_status,name="url_status"),
    path('internet_block_input',views.internet_block_input,name="internet_block_input"),
    path('internet_block',views.internet_block,name="internet_block"),
    #path('url_status_invalid',views.url_status,name="url_status")
    #html page name, views, viewscheck
]
