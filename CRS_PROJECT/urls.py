"""CRS_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import CRS_APP.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CRS_APP.views.home, name='home'),  
    path('main/',CRS_APP.views.main, name = 'main'),
    path('chatbot/',CRS_APP.views.chatbot, name = 'chatbot'),
    path('introduce/',CRS_APP.views.introduce, name = 'introduce'),
    path('search/',CRS_APP.views.search, name = 'search'),
    path('contactUs/',CRS_APP.views.contactUs, name = 'contactUs'),
    path('result/',CRS_APP.views.result, name = 'result'),
]


