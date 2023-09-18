from rest_framework import serializers


class CurrencyConversionSerializer(serializers.Serializer):
    base_currency = serializers.CharField(required=True, max_length=3)
    currencies = serializers.CharField(required=True, max_length=3)
    many = serializers.FloatField(required=True, min_value=0)
    data = serializers.FloatField(required=False)
