from rest_framework import serializers

from .models import Data

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('id','user_ID','keyin','input','score')
        
