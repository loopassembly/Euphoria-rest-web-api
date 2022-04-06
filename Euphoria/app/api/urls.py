from django.urls import include, path

from rest_framework import routers, views
from rest_framework.routers import DefaultRouter

from .views import SingerViewSet,SongViewSet,MenuViewSet,HotelViewSet

router = routers.DefaultRouter()
router.register('Song', SongViewSet)
router.register('Singer', SingerViewSet)
router.register('Menu', MenuViewSet)
router.register('Hotel', HotelViewSet)

urlpatterns = [
   path('', include(router.urls)),
]