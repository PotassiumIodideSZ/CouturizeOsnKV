from rest_framework import serializers
from .models import BodyType, ClothingRecommendations, UserProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = '__all__'

class ClothingRecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingRecommendations
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    body_type = BodyTypeSerializer(read_only=True)
    recommendations = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = (
            'id', 'user', 'body_type', 'preferred_style',
            'chest', 'waist', 'hips', 'height',
            'recommendations', 'created_at', 'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at', 'body_type', 'user')

    def get_recommendations(self, obj):
        if obj.body_type:
            recommendation = ClothingRecommendations.objects.filter(body_type=obj.body_type).first()
            if recommendation:
                return ClothingRecommendationsSerializer(recommendation).data
        return None

    def update(self, instance, validated_data):
        # Обновляем измерения без вызова save() для предотвращения рекурсии
        if 'chest' in validated_data:
            instance.chest = validated_data['chest']
        if 'waist' in validated_data:
            instance.waist = validated_data['waist']
        if 'hips' in validated_data:
            instance.hips = validated_data['hips']
        if 'height' in validated_data:
            instance.height = validated_data['height']
        if 'preferred_style' in validated_data:
            instance.preferred_style = validated_data['preferred_style']
        
        # Напрямую обновляем тип тела
        from .models import BodyType
        
        # Проверяем, есть ли все необходимые измерения
        if all([instance.chest, instance.waist, instance.hips]):
            chest_hips_diff = abs(float(instance.chest) - float(instance.hips))
            chest_waist_diff = float(instance.chest) - float(instance.waist)
            hips_waist_diff = float(instance.hips) - float(instance.waist)
            
            # Определение типа фигуры
            if chest_hips_diff <= 5 and chest_waist_diff >= 20:
                body_type_name = "Песочные часы"
            elif chest_hips_diff <= 5 and chest_waist_diff < 19:
                body_type_name = "Прямоугольник"
            elif chest_hips_diff >= 10:
                body_type_name = "Треугольник"
            else:
                body_type_name = "Яблоко"
            
            # Находим соответствующий тип тела
            body_type, _ = BodyType.objects.get_or_create(name=body_type_name)
            instance.body_type = body_type
        
        # Используем direct database update для предотвращения рекурсии
        from django.db.models import Q
        UserProfile.objects.filter(pk=instance.pk).update(
            chest=instance.chest,
            waist=instance.waist,
            hips=instance.hips,
            height=instance.height,
            preferred_style=instance.preferred_style,
            body_type=instance.body_type
        )
        
        return instance
