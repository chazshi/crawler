from rest_framework import serializers
from Infos.models import Infos

# serializers.Serializer会转换不了json
class InfosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infos
        fields = ('id','city','title', 'time', 'link')


class CitysSerializer(serializers.ModelSerializer):
    city = serializers.CharField(max_length=10)
    class Meta:
        model = Infos
        fields = ('city',)
