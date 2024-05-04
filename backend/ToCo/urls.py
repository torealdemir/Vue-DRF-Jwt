from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('',views.ContentListViewSet, basename='MainContent')

urlpatterns = [
    path("", include(router.urls)),
    # path("addproject/", views.ProjectCreateApiView.as_view()),
    # path("projects/delete/<int:pk>/", views.BlogDeleteApiView.as_view()),
]

urlpatterns += router.urls


# from django.urls import path
# from blog import views
# from rest_framework import routers
# from . import views


# router = routers.DefaultRouter()
# router.register('', views.BlogListViewset, basename="all-blogs")

# urlpatterns = [
#     path('addblog/', views.BlogCreateAPIView.as_view()),
#     path('deleteblog/<int:pk>/', views.BlogDeleteApiView.as_view()),
# ]

# urlpatterns += router.urls