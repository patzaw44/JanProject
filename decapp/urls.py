from django.urls import path, include
from rest_framework import routers
from DecCars.decapp import views
from DecCars.decapp.views import test_response, create_car, test_heading


router = routers.DefaultRouter()
router.register(r'cars', views.AutoViewSet, 'Car data')
router.register(r'carss', views.AutoDelViewSet, 'Deltest')
router.register(r'rate', views.RateViewSet, 'Ratetest')
router.register(r'carsall', views.AllAutoViewSet, 'All Cars')
router.register(r'popular', views.PopularAutoViewSet, 'Popular cars')


urlpatterns = [
    path('test/', test_response),
    path('tests/', test_heading),
    path('new/', create_car),
    path('', include(router.urls))
]
