"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view
from pages.views import contact_view, social_view
from products.views import product_detail_view, product_create_view
from neo.views import neo_create_view, neo_create_id_view, neo_delete_id_view, neo_list_view

urlpatterns = [
    path('neo/', include('neo.urls')),
    path('blog/', include('blog.urls')),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('social/', social_view, name='social'),
    path('create/', product_create_view, name='product_create'),
    path('product/', product_detail_view, name='product_detail'),
    path('admin/', admin.site.urls),
    


    # path('neo/', neo_create_view, name='neo_create'),
    # path('neo/<int:my_id>/', neo_create_id_view, name='neo_create_id'),
    # path('neo/<int:my_id>/delete/', neo_delete_id_view, name='neo_delete_id'),
    # path('neo/list/', neo_list_view, name='neo_list'),
    
]
