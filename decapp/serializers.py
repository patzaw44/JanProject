from .models import Car, Rate
from rest_framework import serializers


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('make', 'model')


class AutoDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'model')


class AutoAllSerializer(serializers.HyperlinkedModelSerializer):
        avg_rating = serializers.SerializerMethodField()

        class Meta:
            model = Car
            fields = ('id', 'make', 'model', 'avg_rating')

        def get_avg_rating(self, obj):
            return obj.avg_rating

        # def get_avg_rating(self, obj):
        #     if obj.rating >4:
        #         return "Good"
        #     else:
        #         return "Keep going"


class RateSerializer(serializers.HyperlinkedModelSerializer):
    car_id = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    rating = serializers.IntegerField()

    class Meta:
        model = Rate
        fields = ('car_id', 'rating')


class PopularSerializer(serializers.ModelSerializer):
    rates_number = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'rates_number')

    def get_rates_number(self, obj):
        return obj.rates_number


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id', 'car_id', 'rating')

