from django.utils import timezone
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('phone_number', 'bio', 'date_birthday')

    def validate_phone_number(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError(
                "Mobile phone is required."
            )

        value = value.strip()

        if not value.isdigit():
            raise serializers.ValidationError(
                "Mobile phone must contain only digits."
            )

        if len(value) != 11:
            raise serializers.ValidationError(
                "Mobile phone must have 11 digits."
            )

        if Profile.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                "Mobile phone already exists."
            )

        return value

    def validate_date_birthday(self, value):
        today = timezone.localdate()

        if value > today:
            raise serializers.ValidationError(
                "Birthday cannot be in the future."
            )

        age = (
            today.year
            - value.year
            - ((today.month, today.day) < (value.month, value.day))
        )

        if age < 13:
            raise serializers.ValidationError(
                "You must be at least 13 years old."
            )

        return value