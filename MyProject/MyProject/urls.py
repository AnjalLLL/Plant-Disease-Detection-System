"""
URL configuration for My_Project project.

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
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from myapp import views
from bson import ObjectId
def user_id_pattern(value):
    try:
        return str(ObjectId(value))
    except:
        raise ValueError("Invalid ObjectId format")

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', include("myapp.urls")),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'), 
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
    path('profile/', views.profile, name='user_profile'),
    path('updateprofile/', views.update_profile, name='update_profile'),
    path('image/<str:file_id>/', views.view_image, name='view_image'),
    
   # path("get_full_info/", views.get_full_info, name="get_full_info"),
    #path('disease_info/', views.disease_info, name='disease_info'),
    
    path('logout/', views.logout, name='logout'),

    
    # path('logout/', views.logout, name='logout'),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)