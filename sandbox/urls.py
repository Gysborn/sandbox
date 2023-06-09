from django.conf.urls.static import static
from sandbox import settings

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('authentication.urls', 'user'))),
    path('post/', include(('post.urls', 'post'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
