from django.forms import ValidationError
from django.utils import timezone
from rest_framework import serializers
from bookings.models import Booking


class CreateExperienceBookingSerializer(serializers.ModelSerializer):
    experience_time = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "experience_time",
            "guests",
        )

    def validate_experience_time(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")

        experience = self.context["experience"]
        print(experience)
        if experience.bookings.filter(experience_time=value).exists():
            raise ValidationError("This experience is already taken")
        return value


class CreateRoomBookingSerializer(serializers.ModelSerializer):
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        else:
            return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        else:
            return value

    def validate(self, data):
        if data["check_out"] < data["check_in"]:
            raise serializers.ValidationError(
                "Check in should be samller than check out!"
            )
        if Booking.objects.filter(
            check_in__lt=data["check_out"], check_out__gt=data["check_in"]
        ).exists():
            raise serializers.ValidationError("Those of those dates are already taken.")
        return data


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )
