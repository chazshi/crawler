from rest_framework import serializers
from City.models import Anqing
from City.models import Hefei

# serializers.Serializer会转换不了json
class AnqingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anqing
        fields = ('title', 'time', 'link')

class HefeiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hefei
        fields = ('title', 'time', 'link')