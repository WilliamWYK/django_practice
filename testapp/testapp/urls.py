"""testapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views
from restaurants.views import menu, list_restaurants, comment, delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<slug:name>/',views.hello),
    re_path(r'^(\d{1,3})/plus/(\d{1,2})/$',views.add),
    path('<int:a>/math/<int:b>/',views.math),
    path('menu/',menu),
    path('restaurant_list/',list_restaurants,name='restaurant_list'),
    path('welcome/',views.welcome),
    path('meta/',views.meta),
    path('comment/',comment),
    path('delete/',delete),
    path ('use_seesion/',views.use_session),
    path('accounts/login/',auth_views.LoginView.as_view(),name='login') ,  # Redirect address set at settings
    path('index/',views.home,name='home'),
    path('accounts/logout/',views.logout,name='logout'),
]
