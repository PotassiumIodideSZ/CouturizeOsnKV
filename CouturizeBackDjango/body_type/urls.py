from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'body-types', views.BodyTypeViewSet)
router.register(r'recommendations', views.ClothingRecommendationsViewSet)
router.register(r'profiles', views.UserProfileViewSet, basename='profiles')

urlpatterns = [
    path('', include(router.urls)),
]
