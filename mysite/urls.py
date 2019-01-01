"""mysite URL Configuration

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
from django.urls import path,re_path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'show_time/', views.show_time),
    # 只有分组的东西才有参数,无命名分组
    re_path(r'article/(\d{4})$',views.article),
    # 有名分组
    re_path(r'article/(?P<year>\d{4})/(?P<month>\d{2})',views.articles),
    re_path(r'register/',views.register,name="reg"),
    re_path(r"query/",views.query)
]
