from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('',views.ContentListViewSet, basename='MainContent')

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += router.urls
