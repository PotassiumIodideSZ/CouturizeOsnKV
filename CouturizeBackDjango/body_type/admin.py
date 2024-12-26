from django.contrib import admin
from .models import BodyType, ClothingRecommendations, UserProfile

@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(ClothingRecommendations)
class ClothingRecommendationsAdmin(admin.ModelAdmin):
    list_display = ('body_type', 'suitable_clothes', 'unsuitable_clothes')
    list_filter = ('body_type',)
    search_fields = ('body_type__name',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'body_type', 'chest', 'waist', 'hips', 'height', 'created_at', 'updated_at')
    list_filter = ('body_type',)
    search_fields = ('user__username', 'body_type__name')
    readonly_fields = ('created_at', 'updated_at')
