
"""DRFapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from api import views
from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
#
# router.register('userapi', views.UserViewSet, basename = 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.UserList.as_view()),
    path('api/<int:pk>', views.UserListRUD.as_view()),
    # path('apiCreate/', views.UserListCreate.as_view()),
    # path('apiRetrieve/<int:pk>', views.UserListRetrieve.as_view()),
    # path('apiUpdate/<int:pk>', views.UserListUpdate.as_view()),
    # path('apiDelete/<int:pk>', views.UserListDestroy.as_view()),


]
