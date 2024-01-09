from rest_framework import serializers

from users.models import User


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )


class PrivateUserSerializer(serializers.ModelSerializer):
    roomsCount = serializers.SerializerMethodField()
    reviewsCount = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "avatar",
            "name",
            "is_host",
            "gender",
            "roomsCount",
            "reviewsCount",
        )

    def get_roomsCount(self, user):
        return user.rooms.count()

    def get_reviewsCount(self, user):
        return user.reviews.count()
