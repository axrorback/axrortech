from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/',include('django_ckeditor_5.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('', include('asosiy.urls')),

]
