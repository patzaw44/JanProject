from django.urls import path, include
from rest_framework import routers
from DecCars.decapp import views
from DecCars.decapp.views import test_response, create_car, test_heading, RatingView

router = routers.DefaultRouter()
router.register(r'car', views.AutoViewSet, 'Car data')
router.register(r'testid', views.TestViewSet, 'Deltest')
router.register(r'rate', views.RateViewSet, 'Ratetest')
router.register(r'cars', views.AllAutoViewSet, 'List Cars')
router.register(r'popular', views.PopularViewSet, 'Popular cars')


urlpatterns = [
    path('test/', test_response),
    path('tests/', test_heading),
    path('new/', create_car),
    path('', include(router.urls)),
    path('stats/', RatingView.as_view()),
]
