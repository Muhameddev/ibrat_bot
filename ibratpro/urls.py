
from django.contrib import admin
from django.urls import path
from ibratapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-ibrat/', admin.site.urls),
    path('nom/', NomView.as_view(), name="nom"),
    path('video/', VideoView.as_view(), name="video"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
