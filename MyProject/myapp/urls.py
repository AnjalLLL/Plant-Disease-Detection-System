from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'), 
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
   # path("get_full_info/", views.get_full_info, name="get_full_info"),
   # path('disease_info/', views.disease_info, name='disease_info'),
    path('logout/', views.logout, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)