from django.db import models
from django.contrib.auth.models import User

class BodyType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class ClothingRecommendations(models.Model):
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, related_name='recommendations')
    suitable_clothes = models.TextField()
    unsuitable_clothes = models.TextField()
    general_recommendations = models.TextField()

    def __str__(self):
        return f"Recommendations for {self.body_type.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    preferred_style = models.TextField(null=True, blank=True)
    
    # Measurements
    chest = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    waist = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    hips = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile for {self.user.username}"

    def update_body_type(self):
        if not all([self.chest, self.waist, self.hips]):  # если не все измерения заполнены
            return None

        chest_hips_diff = abs(float(self.chest) - float(self.hips))
        chest_waist_diff = float(self.chest) - float(self.waist)
        hips_waist_diff = float(self.hips) - float(self.waist)
        hips_chest_diff = float(self.hips) - float(self.chest)

        # Определение типа фигуры на основе измерений
        if chest_hips_diff <= 5 and chest_waist_diff >= 20:
            body_type_name = "Песочные часы"
        elif chest_hips_diff <= 5 and chest_waist_diff < 19:
            body_type_name = "Прямоугольник"
        elif hips_chest_diff >= 10 and hips_waist_diff >= 20:
            body_type_name = "Треугольник"
        elif chest_hips_diff >= 10 and 10 <= chest_waist_diff <= 20:
            body_type_name = "Яблоко"
        elif hips_chest_diff >= 15 and hips_waist_diff >= 20:
            body_type_name = "Груша"
        else:
            body_type_name = "Прямоугольник"  # дефолтный тип фигуры

        body_type, _ = BodyType.objects.get_or_create(name=body_type_name)
        self.body_type = body_type
        self.save()
        return body_type

    def save(self, *args, **kwargs):
        if self.chest and self.waist and self.hips:  # если есть все измерения
            self.update_body_type()
        super().save(*args, **kwargs)
