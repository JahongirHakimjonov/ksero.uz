from rest_framework import serializers
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.shared.utils.authentication import UniversalPasswordAuthentication
from apps.users.models.users import ActiveSessions


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    phone_number_field = "phone"

    def validate(self, attrs):
        credentials = {
            "phone": attrs.get(self.phone_number_field),
            "password": attrs.get("password"),
        }

        user = UniversalPasswordAuthentication.authenticate(
            credentials["phone"], credentials["password"]
        )
        if user:
            tokens = UniversalPasswordAuthentication.generate_tokens(user)

        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        return tokens


class CustomTokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        refresh = attrs.get("refresh")

        if refresh is None:
            raise serializers.ValidationError("No refresh token provided")

        return {"refresh": refresh}


class BlockSessionSerializer(serializers.Serializer):
    session_id = serializers.IntegerField()


class ActiveSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveSessions
        fields = (
            "id",
            "user",
            "ip",
            "user_agent",
            "location",
            "last_activity",
        )
