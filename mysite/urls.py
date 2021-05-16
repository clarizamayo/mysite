from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('database/', views.listing, name='listing'),
    path('contact/', views.adoption, name='adoption'),
    path('chart/', views.chartpath, name='chart'),
]
