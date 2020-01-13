"""snet4 URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from users import views as user_views
from django.conf import settings 
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('feed.urls')),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('signup/',user_views.UserRegView.as_view(), name='signup'),
    path('profile/',user_views.profile, name='profile'),
    path('rprofile/<int:id>/',user_views.rprofile, name='rprofile'),
    path('accept/',user_views.friend_req, name='accept'),
    path('pchange/',
        PasswordChangeView.as_view(template_name='users/pchange.html'), 
        name='pchange'),
    path('pcdone/',PasswordChangeDoneView.as_view(template_name='users/pcdone.html'), name='password_change_done')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
