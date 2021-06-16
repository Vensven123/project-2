from django.contrib import admin
from django.urls import path
from django.conf.urls import include

#from quitzapp import views


urlpatterns = [
    path('admin/',admin.site.urls),
    #path('welcome',views.welcome),
    path('welcome/',include('quitzapp.urls')),
]
