from django.db.models import Avg, Count
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from DecCars.decapp.forms import AutoForm
from DecCars.decapp.models import Car, Rate
from DecCars.decapp.serializers import AutoSerializer, AutoDelSerializer, AutoAllSerializer, \
    PopularSerializer, RateSerializer, RatingSerializer


def test_response(request):
    return HttpResponse("Cars app")


def test_heading(request):
    auto_all = Car.objects.all()
    # number = len(auto_all)
    return render(request, 'auto.html', {'text': auto_all})


def create_car(request):
    form = AutoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'new_car.html', {'form': form})


class AutoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Car.objects.all()
    serializer_class = AutoSerializer

    def list(self, request, *args, **kwargs):
        """GET car list"""
        queryset = self.get_queryset()
        serializer = AutoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """POST car"""
        car = Car.objects.create(make=request.data['make'], model=request.data['model'])
        serializer = AutoSerializer(car, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """DEL car/{id}"""
        car = self.get_object()
        self.perform_destroy(car)
        # car.delete()
        return Response(f"Successfully deleted")


class TestViewSet(viewsets.ModelViewSet):
    """
 test
    """

    def get_queryset(self):
        queryset_id = Car.objects.filter(id=2)
        return queryset_id
    serializer_class = AutoDelSerializer


class RateViewSet(viewsets.ModelViewSet):
    """Add rate for car (scale: 1-5)"""
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def list(self, request, *args, **kwargs):
        """GET rate list"""
        queryset = self.get_queryset()
        serializer = RateSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """POST rate"""
        rate = Rate.objects.create(car_id=request.data["car_id"], rating=request.data["rating"])
        serializer = RateSerializer(rate, many=False)
        return Response(serializer.data)


class RatingView(APIView):
    serializer_class = RatingSerializer
    queryset = Rate.objects.all()

    #     data = {}
    #     for car in Car.objects.all():
    #         car = Rate.objects.filter(id=Rate.car_id).aggregate(avg_rating=Avg("rating"))
    #
    #         # cars_id = Car.id('id', flat=True)
    #         # data = Auto.objects.filter(model=model).include(id=id)
    #         # data = data.annotate(avg_rating=Count("new_rate__rating"))

    #     return Response(data=data)


class AllAutoViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = AutoAllSerializer

    # def get_queryset(self):
    # queryset = Car.objects.filter(model="Golf")

    def get_queryset(self):
        self.queryset = self.queryset.annotate(avg_rating=Avg("new_rate__rating"))
        self.queryset = self.queryset.annotate(rates_number2=Count("new_rate__rating"))
        return self.queryset

    def list(self, request, *args, **kwargs):
        """GET list cars"""
        queryset = self.get_queryset()
        serializer = AutoAllSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """GET /cars/{id}"""
        instance = self.get_object()
        serializer = AutoDelSerializer(instance)
        return Response(serializer.data)

# @action(detail=False, methods="post")
# def avgrate(self, request, rating, **kwargs):
#     rating = Rate.rating.get_object()
#     n_rate = Car.objects.all()
#     avg_rating = sum(rating) / len(rating)
#     n_rate.update(avg_rating=request.data['avg_rating'])
#     # n_rate.save()
#     # car = car.avg_rating.create(avg_rating=request.data[avg_rating])
#     serializer = AutoAllSerializer(n_rate, many=True)
#     return Response(serializer.data)


class PopularViewSet(viewsets.ModelViewSet):
        queryset = Car.objects.all()
        serializer_class = PopularSerializer

        def get_queryset(self):
            self.queryset = self.queryset.annotate(avg_rating=Count("new_rate__rating"))
            # self.queryset = self.queryset.aggregate(Avg('rating'))
            self.queryset = self.queryset.annotate(rates_number=Count("new_rate__rating")).order_by("-rates_number")
            return self.queryset

            # number = 0
            # rates_number = Rate.rating[0]
            # for car_id in Rate.rating:
            #     freq = Rate.rating.count(car_id)
            #     if freq > number:
            #         number = freq
            #         rates_number = car_id
