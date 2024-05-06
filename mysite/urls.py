"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin,auth
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from magasin.views import index
from magasin import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView
from django.conf.urls import handler404
router = routers.SimpleRouter()
router.register('product', ProductViewset, basename='product')
urlpatterns = [
    path("admin/", admin.site.urls),
    path('magasin/',include('magasin.urls')),
    path("blog/",include('blog.urls')),
    path('',index),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name ='logout'),
path('api-auth/', include('rest_framework.urls')),
path('api/', include(router.urls)),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
handler404 = 'magasin.views.handler404'