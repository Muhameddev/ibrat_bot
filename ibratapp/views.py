from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *


class NomView(ListCreateAPIView):
    queryset = Nom.objects.all()
    serializer_class = Nomser

class VideoView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = Videoser


