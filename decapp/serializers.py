from .models import Auto, NewRate
from rest_framework import serializers


class AutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auto
        fields = ['make', 'model']


class AutoDelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auto
        fields = ['id', 'model']


class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewRate
        fields = ['car_rate', 'rating']


class AutoAllSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auto
        fields = ['id', 'make', 'model', 'avg_rating']


class PopularSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auto
        fields = ['id', 'make', 'model', 'rates_number']
