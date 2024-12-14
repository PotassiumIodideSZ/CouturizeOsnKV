from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import BodyType, ClothingRecommendations, UserProfile
from .serializers import (
    BodyTypeSerializer,
    ClothingRecommendationsSerializer,
    UserProfileSerializer
)

class BodyTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BodyType.objects.all()
    serializer_class = BodyTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = self.queryset
        body_type_id = self.request.query_params.get('body_type_id')
        if body_type_id:
            queryset = queryset.filter(id=body_type_id)
        return queryset

class ClothingRecommendationsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClothingRecommendations.objects.all()
    serializer_class = ClothingRecommendationsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        body_type_id = request.query_params.get('body_type_id')
        if body_type_id:
            queryset = self.queryset.filter(body_type_id=body_type_id)
        else:
            queryset = self.queryset
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def by_body_type(self, request):
        body_type_id = request.query_params.get('body_type_id')
        if not body_type_id:
            return Response(
                {"error": "body_type_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        recommendations = self.queryset.filter(body_type_id=body_type_id)
        serializer = self.get_serializer(recommendations, many=True)
        return Response(serializer.data)

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    @action(detail=False, methods=['GET'])
    def my_profile(self, request):
        profile = get_object_or_404(UserProfile, user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

    @action(detail=False, methods=['PATCH'])
    def update_measurements(self, request):
        profile = get_object_or_404(UserProfile, user=request.user)
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def my_recommendations(self, request):
        profile = get_object_or_404(UserProfile, user=request.user)
        if not profile.body_type:
            return Response(
                {"error": "Body type not determined yet. Please add your measurements."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        recommendations = ClothingRecommendations.objects.filter(body_type=profile.body_type).first()
        if not recommendations:
            return Response(
                {"error": "No recommendations found for your body type."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ClothingRecommendationsSerializer(recommendations)
        return Response(serializer.data)
