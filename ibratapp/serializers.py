from .models import *

from rest_framework.serializers import ModelSerializer


class Nomser(ModelSerializer):
    class Meta:
        model = Nom
        fields = "__all__"

class Videoser(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
