from rest_framework import serializers
from bookings.models import Booking
from categories.serializers import CategorySerializer
from experiences.models import Experience, Perk
from medias.serializers import PhotoSerializer
from users.serializers import TinyUserSerializer


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        exclude = (
            "created_at",
            "updated_at",
            "id",
        )


class PublicExperienceBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "name",
            "host",
            "start",
            "end",
        )


class ExperienceSerializer(serializers.ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    perks = PerkSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Experience

        exclude = (
            "created_at",
            "updated_at",
        )


class ExperienceDetailSerializer(serializers.ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    perks = PerkSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Experience
        exclude = (
            "created_at",
            "updated_at",
            "category",
        )
