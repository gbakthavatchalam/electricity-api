from rest_framework import serializers

from electricity_api.models import Days, Months


class DaysSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateField()

    class Meta:
        model = Days
        fields = ("consumption", "temperature", "timestamp")


class MonthsSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateField()

    class Meta:
        model = Months
        fields = ("consumption", "temperature", "timestamp")
