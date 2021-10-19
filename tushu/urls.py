"""tushu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from bookinfor.views import AuthorViewSet, SortViewSet, PublishViewSet, BookinforViewSet, BookmemberViewSet, ConsumeViewSet, InoutrecordViewSet


router = DefaultRouter()
router.register(r'author', AuthorViewSet)
router.register(r'sort', SortViewSet)
router.register(r'publish', PublishViewSet)
router.register(r'bookinfor', BookinforViewSet)
router.register(r'bookmember', BookmemberViewSet)
router.register(r'consume', ConsumeViewSet)
router.register(r'inoutrecord', InoutrecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='admin/login.html')),
    path('accounts/logout/', auth_views.LogoutView.as_view()),
    path('', include('bookinfor.urls')),

    # drf 自动注册路由
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
