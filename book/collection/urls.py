from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .viewset import BookViewset

router = DefaultRouter()
router.register('book',BookViewset,basename='BookViewset')


urlpatterns = [
    path("", include(router.urls)),

]
