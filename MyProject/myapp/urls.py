from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'), 
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
    # path('logout/', views.logout, name='logout'),
]