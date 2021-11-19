"""photo_gallery URL Configuration

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
from django.urls import path
from testapp import views
from django.conf import settings ##  accessing settings
from django.conf.urls.static import static
from testapp.models import Category,Photo

urlpatterns = [
    path ('',views.HomeView,name = 'gallery'),
    path ('photos/<str:c>/',views.PhotoListView),
    path ('gallery/',views.galleryView),
    path ('photo/<int:id>/',views.PhotoView),
    path ('add_photo/',views.AddPhotoView),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)    ## settings.MEDIA_URL  >> points to "images folder"... settings.MEDIA_ROOT  >>, points to "static/images" directory
