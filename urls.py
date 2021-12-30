from django.contrib import admin
from django.urls import path, include
# from DecCars.decapp.views import test_response
# from django.conf.urls import include
# from . import decapp
# from .decapp import urls
# from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DecCars.decapp.urls'))
]