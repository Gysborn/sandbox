from rest_framework import serializers
from authentication.models import User
from authentication.validators import MinimumLengthValidator, NumericInPasswordValidator, EmailValidator


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["is_staff", "is_superuser", "is_active", "groups", "user_permissions"]

    birthday = serializers.DateField(required=True)
    password = serializers.CharField(
        max_length=128,
        validators=[
            MinimumLengthValidator(),
            NumericInPasswordValidator(),
            ]
    )
    email = serializers.EmailField(required=True, validators=[EmailValidator()])

    def create(self, validated_data):  # Переопределяем метод сэйв что бы пароли шифровались
        user = super().create(validated_data)
        user.set_password(user.password)  # Здесь шифруем пароль
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["is_staff", "is_superuser", "is_active", "groups", "user_permissions", "password"]


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
