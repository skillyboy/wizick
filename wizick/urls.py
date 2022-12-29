from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('dmsstaff/', admin.site.urls),
    path('', include('dms.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('tinymce/', include('tinymce.urls')),
    # path('api-auth/', include('rest_framework.urls'))

]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
