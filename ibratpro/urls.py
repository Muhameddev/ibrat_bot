
from django.contrib import admin
from django.urls import path
from ibratapp.views import *

urlpatterns = [
    path('admin-ibrat/', admin.site.urls),
    path('nom/', NomView.as_view(), name="nom"),
    path('video/', VideoView.as_view(), name="video"),
]
